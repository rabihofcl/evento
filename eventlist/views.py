from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from account.models import User
from eventlist.models import EventList

from .serializers import EventListSerializer
# Create your views here.



class EventListAV(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = User.objects.get(email=request.user)
        eventlists = EventList.objects.filter(user=request.user)

        serializer = EventListSerializer(eventlists, many=True)

        return Response({
            "eventlist": serializer.data
        })


    def post(self, request):

        serializer = EventListSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({
                "success": serializer.data
            })
        else:
            return Response({
                "error": serializer.errors
            })
