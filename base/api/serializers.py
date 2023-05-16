"""
Serializers are the classes that take a certain model to serialize a certain object and turn it to json data.
"""
from rest_framework.serializers import ModelSerializer
from base.models import Room


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
