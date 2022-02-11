from rest_framework import serializers
from .models import EventList


class EventListSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventList
        fields = ['event_name', 'event_date']


class EventListSerializerAll(serializers.ModelSerializer):

    class Meta:
        model = EventList
        fields = '__all__'