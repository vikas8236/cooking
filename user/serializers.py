# from rest_framework import serializers
# from .models import Student
# from django.contrib.auth.hashers import make_password, check_password

# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ['id', 'FirstName', 'LastName', 'Email', 'Password']

#     def create(self, validated_data):
#         validated_data['Password'] = make_password(validated_data['Password'])
#         return super(StudentSerializer, self).create(validated_data)

# class LoginSerializer(serializers.Serializer):
#     Email = serializers.EmailField()
#     Password = serializers.CharField()
# serializers.py


from rest_framework import serializers
from .models import Student
from django.contrib.auth.hashers import make_password

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [ 'firstname', 'lastname', 'age', 'email', 'password']
        
    def validate_age(self, value):
        if value <= 17 or value > 100:
            raise serializers.ValidationError('Enter a valid age')
        return value  
    
    def validate_firstname(self, value):
        if not value.isalpha():
            raise serializers.ValidationError('firstname is not valid! try again')
        return value
    
    def validate_lastname(self, value):
        if not value.isalpha():
            raise serializers.ValidationError('lastname is not valid! try again')
        return value
    
    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError('Email cannot be null')
        if not value.endswith("@gmail.com"):
            raise serializers.ValidationError("Email must end with @gmail.com")
        return value
    def validate_password(self, value):
        
        if len(value) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters long')
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError('Password must contain at least one digit')
        if not any(char.isalpha() for char in value):
            raise serializers.ValidationError('Password must contain at least one letter')
        return value


    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()



class OTPRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()


class OTPVerifySerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)























