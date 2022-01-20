from rest_framework import serializers
from .models import User
import re



class UserSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'phone_number', 'password', 'password2']

        extra_kwargs = {
            'password' : {'write_only': True}
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        email = self.validated_data['email']
        phone_number = self.validated_data['phone_number']

        if password != password2:
            raise serializers.ValidationError("Password is not matching")
        else:
            if email:
                if User.objects.filter(email=self.validated_data['email']).exists():
                    raise serializers.ValidationError("Email is already exists")
            if phone_number:
                if User.objects.filter(phone_number=self.validated_data['phone_number']).exists():
                    raise serializers.ValidationError("Phone number is already exists")
            if password:
                reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

                # compiling regex
                pattern = re.compile(reg)

                # searching regex                 
                match = re.search(pattern, password)

                # validating conditions
                if match == None:
                    raise serializers.ValidationError("Password should contain Uppercase, Lowercase, Numeric and Special Characters.")

        user = User(
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            username = self.validated_data['username'],
            email = self.validated_data['email'],
            phone_number = self.validated_data['phone_number']
        )
        user.set_password(password)
        user.save()

        return user


        

    # def validate_email(self, value):
    #     reg = "/\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b/i"
    #     pattern = re.compile(reg)
    #     match = re.search(pattern, value)
    #     print('1')
    #     if match:
            
    #         print('2')
    #         return value
    #     else:
    #         print('3')
    #         raise serializers.ValidationError("Invalid Email")
        



    # def validate_username(self, value):
    #     if len(value) < 3:
    #         raise serializers.ValidationError("Username is too short")
    #     else:
    #         return value

    # def validate_password(self, value):

    #     if len(value) < 8:
    #         raise serializers.ValidationError("Password should contain atleast 8 characters")
    #     else:
    #         password = value
    #         reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

    #         # compiling regex
    #         pattern = re.compile(reg)

    #         # searching regex                 
    #         match = re.search(pattern, password)

    #         # validating conditions
    #         if match:
    #             return value
    #         else:
    #             raise serializers.ValidationError("Password should contain Uppercase, Lowercase, Numeric and Special Characters.")


        