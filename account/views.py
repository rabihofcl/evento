from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.


class UserRegisterAV(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = serializer.data
            return Response({
                "user": serializer.data,
                "message": "Registered Successfully.  Now perform Login to get your token",
            })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        