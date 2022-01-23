from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Professionals
from .serializers import ProfessionalsSerializer
from accounts.models import User
from rest_framework import status

# Create your views here.



class ProfessionalsRegisterAV(APIView):

    def post(self, request):
        serializer = ProfessionalsSerializer(data=request.data)
        if Professionals.objects.filter(user=request.user):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)