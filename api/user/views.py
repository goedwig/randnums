from rest_framework import generics, throttling
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
    class NumberRegenerationUserRateThrottle(throttling.UserRateThrottle):
        scope = 'number_regeneration'

        def allow_request(self, request, view):
            if request.method != 'PUT':
                return True
            return super().allow_request(request, view)

    queryset = RandomizedNumber.objects.all()
    serializer_class = GenerationSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        custom_permissions.IsRandomizedNumberOwner,
    ]
    throttle_classes = [NumberRegenerationUserRateThrottle]

    def get_queryset(self):
        return RandomizedNumber.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(value=Randomizer.number())
