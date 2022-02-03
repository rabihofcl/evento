from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
import datetime 
from datetime import timedelta

from .models import Vendor
from .serializers import VendorSerializer, VendorSerializerAll
from account.models import User
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

# Create your views here.


class VendorRegisterCheckAV(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = User.objects.get(email=request.user)
        if user.is_staff:
            return Response({
                "success": "User is Vendor"
            })
        else:
            return Response({
                "error":"User is not a vendor"
            })


class VendorRegisterAV(APIView):

    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]


    def get(self, request):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        if Vendor.objects.filter(user = request.user).exists():
            return Response({
                "error": "Vendor already Registered"
            })

        else:
            user = User.objects.get(email = request.user)
            serializer = VendorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                vendor = Vendor.objects.get(user = request.user)
                if vendor.subscription_type == 'monthly':
                    vendor.expiry_date = vendor.subscription_date + timedelta(days=30)
                    vendor.save()
                else:
                    vendor.expiry_date = vendor.subscription_date + timedelta(days=365)
                    vendor.save()
                user.is_staff = True
                user.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)            


class VendorUpdateAV(APIView):

    def get(self, request):
        user = request.user
        serializer = VendorSerializer(user, many=False)      
        return Response(serializer.data)


    def put(self, request):
        user = request.user
        serializer = VendorSerializer(user, many=False)

        data = request.data
        user.full_name = data['full_name']
        user.profile_picture = data['profile_picture']
        user.category = data['category']
        user.place = data['place']
        user.city = data['city']
        user.state = data['state']
        user.pincode = data['pincode']

        user.save()

        return Response(serializer.data)



class VendorHomePageAV(APIView):

    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get(self, request):
        vendor = Vendor.objects.get(user = request.user)
        serializer = VendorSerializerAll(vendor, many=False)


        return Response({
            "vendor": serializer.data
        })


class VendorProfile(APIView):

    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        vendor = Vendor.objects.get(user = request.user)
        serializer = VendorSerializerAll(vendor, many=False)


        return Response({
            "vendor": serializer.data
        })