from rest_framework import generics
from rest_framework import permissions

from api.user.serializers import GenerationSerializer
from common.util.randomizer import Randomizer
from randomizer import permissions as custom_permissions
from randomizer.models import RandomizedNumber


class GenerationsList(generics.ListCreateAPIView):
    queryset = RandomizedNumber.objects.all()
    serializer_class = GenerationSerializer

    def get_queryset(self):
        return RandomizedNumber.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(value=Randomizer.number(), user=self.request.user)


class GenerationsDetail(generics.RetrieveUpdateAPIView):
    queryset = RandomizedNumber.objects.all()
    serializer_class = GenerationSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        custom_permissions.IsRandomizedNumberOwner,
    ]

    def get_queryset(self):
        return RandomizedNumber.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        # TODO: Allow updates only once per hour
        serializer.save(value=Randomizer.number())
