


from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'firstname', 'lastname', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        student = Student.objects.create(
            firstname=validated_data['firstname'],
            lastname=validated_data['lastname'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return student

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()





























