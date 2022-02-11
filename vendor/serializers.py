from rest_framework import serializers
from .models import Vendor, VendorSlots



class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        exclude = [ 'user', 'subscription_date', 'expiry_date' ]


class VendorHomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields = ['name', 'profile_picture']


class VendorSerializerAll(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields = '__all__'

        
class VendorSlotsSerializer(serializers.ModelSerializer):

    class Meta:
        model = VendorSlots
        fields = ['busy_slots']