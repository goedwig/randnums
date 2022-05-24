from django.contrib.auth.models import User
from django.db.models import Max, Avg
from rest_framework import generics, permissions, throttling, views
from rest_framework.response import Response

from api.user.serializers import GenerationSerializer
from common.util.randomizer import Randomizer
from randomizer import permissions as custom_permissions
from randomizer.models import RandomizedNumber


class GenerationsListCreateAPIVIew(generics.ListCreateAPIView):
    queryset = RandomizedNumber.objects.all()
    serializer_class = GenerationSerializer

    def get_queryset(self):
        return RandomizedNumber.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(value=Randomizer.number(), user=self.request.user)


class GenerationsRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
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


class StatsAPIView(views.APIView):
    def get(self, request):
        stats = {}

        qs = RandomizedNumber.objects\
            .filter(user=request.user)\
            .aggregate(Max('value'), Avg('value'))

        stats['max'] = qs['value__max']
        stats['avg'] = qs['value__avg']

        users = User.objects\
            .annotate(avg_value=Avg('generations__value'))\
            .order_by('-avg_value')

        position = None
        for position, user in enumerate(users, start=1):
            if user == request.user:
                break

        stats['position'] = position

        return Response(stats)
