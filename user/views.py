from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .serializers import ProfessionalListSerializer

from vendor.models import Vendor

# Create your views here.


class ProfessionalsListAV(APIView):

    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get(self, request):

        data = request.data
        profession = data['profession']
        # try:
        vendors = Vendor.objects.filter(category = profession)
        serializer = ProfessionalListSerializer(vendors, many=True)
        count = 0
        for k, v in serializer():
            count += 1

        if count == 0:
            return Response({
                "error": "No vendors available"
            })
        else:
            return Response({
                "success": serializer.data
            })
        
        # except:
        #     return Response({
        #         "error": "No vendors"
        #     })
