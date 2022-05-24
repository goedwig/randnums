from rest_framework import serializers

from randomizer.models import RandomizedNumber


class GenerationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RandomizedNumber
        read_only_fields = ['value']
        exclude = ['user']
