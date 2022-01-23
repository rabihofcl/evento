from rest_framework import serializers
from .models import Professionals


class ProfessionalsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professionals
        fields = ['full_name', 'profile_picture', 'place', 'city', 'state', 'pincode']