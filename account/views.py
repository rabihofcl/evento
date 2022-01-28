from django.http import response
from django.shortcuts import render
from decouple import config
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

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
        # print(serializer.errors)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "user": serializer.data,
                "message": "Registered Successfully"
            })
        else:
            print(serializer.errors)
            return Response({
                "error": serializer.errors
            })
        


class RegisterOtpAV(APIView):

    def post(self, request):

        data = request.data
        phone_number = data['phone_number']
        print(phone_number)

        try:
            account_sid = config('account_sid')
            auth_token = config('auth_token')
            client = Client(account_sid, auth_token)

            verification = client.verify \
                .services('VA47f566d6a44e75409506f475d3231b04') \
                .verifications \
                .create(to='+91'+phone_number, channel='sms')

            return Response({
                "success": "Otp send successfully"
            })
        except TwilioRestException:
            return Response({
                "error": "Not a valid phone number"
            })
            



class ConfirmRegisterOtpAV(APIView):

    def post(self, request):

        data = request.data
        phone_number = data['phone_number']
        otp = data['otp']

        account_sid = config('account_sid')
        auth_token = config('auth_token')
        client = Client(account_sid, auth_token)

        verification_check = client.verify \
            .services('VA47f566d6a44e75409506f475d3231b04') \
            .verification_checks \
            .create(to='+91'+phone_number, code=otp)

        if verification_check.status == 'approved':
            user = User.objects.get(phone_number=phone_number)
            user.is_verified = True
            user.save()

            return Response({
                "success":"otp verified"
            })
        else:
            return Response({
                "error": "otp not matching"
            })


        