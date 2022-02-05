from rest_framework import serializers
from vendor.models import Vendor



class ProfessionalListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields = ['name', 'profile_picture', 'place', 'city']