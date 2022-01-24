from rest_framework import serializers
from rest_framework.decorators import  permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Vendor, VendorSubscription




@permission_classes([IsAuthenticated])
class VendorSerializer(serializers.ModelSerializer):

    # _id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Vendor
        fields = [ 'user', 'full_name', 'profile_picture', 'category', 'place', 'city', 'state', 'pincode']


@permission_classes([IsAuthenticated])
class VendorSubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = VendorSubscription
        fields = ['subscription_amount']

