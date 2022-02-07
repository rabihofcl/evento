from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from .serializers import ProfessionalListSerializer, UserHomeSerializer, UserProfileSerializer

from vendor.models import Vendor
from account.models import User

# Create your views here.


class UserHomeAV(APIView):

    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get(self, request):

        try:
            user = User.objects.get(user = request.user)
            serializer = UserHomeSerializer(user, many=False)

            return Response({
                "success": serializer.data
            })
        except:
            return Response({
                "error": serializer.errors
            })


class ProfessionalsListAV(APIView):

    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get(self, request):

        data = request.data
        profession = data['profession']
        
        vendors = Vendor.objects.filter(category = profession)
        serializer = ProfessionalListSerializer(vendors, many=True)

        if len(serializer.data):
            return Response({
                "success": serializer.data
            })
        else:
            return Response({
                "error": "No professionals available"
            })


class UserProfileAV(APIView):

    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser]    

    def get(self, request):

        try:
            user = User.objects.get(user = request.user)
            serializer = UserProfileSerializer(user, many=False)

            return Response({
                "success": serializer.data
            })
        except:
            return Response({
                "error": serializer.errors
            })        