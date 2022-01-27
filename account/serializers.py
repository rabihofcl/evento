from rest_framework import serializers
from .models import User
import re



class UserSerializer(serializers.ModelSerializer):

    # _id = serializers.SerializerMethodField(read_only=True)
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    
    class Meta:
        model = User
        fields = [ 'name', 'username', 'email', 'phone_number', 'password', 'password2']

        extra_kwargs = {
            'password' : {'write_only': True}
        }


    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        email = self.validated_data['email']
        phone_number = self.validated_data['phone_number']

        if password != password2:
            raise serializers.ValidationError({
                        "error":"Password is not matching"
                    })
        else:
            if email:
                if User.objects.filter(email=self.validated_data['email']).exists():
                    raise serializers.ValidationError({
                        "error":"Email is already exists"
                    })
            if phone_number:
                if User.objects.filter(phone_number=self.validated_data['phone_number']).exists():
                    raise serializers.ValidationError({
                        "error":"Phone number is already exists"
                    })
            if password:
                reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

                # compiling regex
                pattern = re.compile(reg)

                # searching regex                 
                match = re.search(pattern, password)

                # validating conditions
                if match == None:
                    raise serializers.ValidationError({
                        "errors":"Password should contain Uppercase, Lowercase, Numeric and Special Characters."
                    })

        user = User(
            name = self.validated_data['name'],
            username = self.validated_data['username'],
            email = self.validated_data['email'],
            phone_number = self.validated_data['phone_number']
        )
        user.set_password(password)
        user.save()

        return user

        