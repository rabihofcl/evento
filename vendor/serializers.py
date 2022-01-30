from rest_framework import serializers
from rest_framework.decorators import  permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Vendor



class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        exclude = [ 'user', 'subscription_date', 'expiry_date' ]



