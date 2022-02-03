from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from .models import Vendor



class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        exclude = [ 'user', 'subscription_date', 'expiry_date' ]

class VendorSerializerAll(serializers.ModelSerializer):

    image_url = serializers.SerializerMethodField('get_image_url')  

    class Meta:
        model = Vendor
        fields = '__all__'

    def get_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.profile_picture.url)