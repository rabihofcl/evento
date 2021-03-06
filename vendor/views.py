import email
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Vendor, VendorSubscription
from .serializers import VendorSerializer, VendorSubscriptionSerializer
from account.models import User
from rest_framework import status

# Create your views here.



class VendorRegisterAV(APIView):

    permission_classes = [IsAuthenticated]


    def get(self, request):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)


    # def post(self, request):

    #     if Vendor.objects.filter(user=request.user):
    #         message = {'detail': 'Already exists'}
    #         return Response(message, status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         serializer = VendorSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save(user=request.user)
    #             return Response(serializer.data)
    #         else:
    #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class VendorRegisterAV(generics.CreateAPIView):
#     queryset = Vendor.objects.all()
#     serializer_class = VendorSerializer
#     permission_classes = [IsAdminUser]


#     def post(self, request, *args, **kwargs):
#         # Note the use of `get_queryset()` instead of `self.queryset`
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



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


class VendorSubscriptionAV(APIView):

    def post(self, request):
        if VendorSubscription.objects.filter(user = request.user):
            message = {'detail': 'User payment already done!'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = VendorSubscriptionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)