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
        responses = {}
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            request.session['phone_number'] = serializer.data['phone_number']
            responses['user'] = serializer.data
            responses['message'] = "Registered Successfully.  Now perform Login to get your token"
            return Response(responses)
        else:
            responses['errors'] = serializer.errors
            
        return Response(responses)


class RegisterOtpAV(APIView):


    def get(self, request):
        if 'phone_number' in request.session:
            phone_number = request.session['phone_number']

            try:
                account_sid = config('account_sid')
                auth_token = config('auth_token')
                client = Client(account_sid, auth_token)

                verification = client.verify \
                    .services('VA47f566d6a44e75409506f475d3231b04') \
                    .verifications \
                    .create(to='+91'+phone_number, channel='sms')
            except TwilioRestException:
                return Response({
                    "error": "Not a valid phone number"
                })

            return Response({
                "success":"otp send successfully"
            })
        else:
            return Response({
                "error":"no phone number in session"
            })



class ConfirmRegisterOtpAV(APIView):

    def post(self, request):
        if 'phone_number' in request.session:
            phone_number = request.session['phone_number']

            data = request.data
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

        else:
            return Response({
                "error":"no phone number in session"
            })

        