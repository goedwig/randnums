from rest_framework import serializers

from randomizer.models import RandomizedNumber


class FeedSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = RandomizedNumber
        read_only_fields = ['value']
        fields = ['value', 'user']
