from rest_framework import generics, permissions, filters

from api.feed.serializers import FeedSerializer
from randomizer.models import RandomizedNumber


class FeedListAPIView(generics.ListAPIView):
    queryset = RandomizedNumber.objects.all()
    serializer_class = FeedSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['user', 'value']
