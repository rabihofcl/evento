from rest_framework import serializers
from account.models import User
from vendor.models import Vendor



class UserHomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['name', 'user_pro_pic']



class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'



class ProfessionalListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields = ['id', 'name', 'profile_picture', 'place', 'city']

