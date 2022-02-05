from rest_framework import serializers
from .models import Vendor



class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        exclude = [ 'user', 'subscription_date', 'expiry_date' ]


class VendorSerializerAll(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields = ['name', 'profile_picture']

