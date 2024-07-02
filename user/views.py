
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer, LoginSerializer
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import AccessToken


class RegisterView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        try:
            student = Student.objects.get(email=email)
        except Student.DoesNotExist:
            return Response({'detail': 'User not found', 'code': 'user_not_found'}, status=status.HTTP_404_NOT_FOUND)

        if student.password != password:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        # Generate and return access token
        access_token = AccessToken.for_user(student)

        return Response({
            'message': "Login successful!",
            'access_token': str(access_token),
        })

# class LoginView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         email = serializer.validated_data['email']
#         password = serializer.validated_data['password']

#         try:
#             student = Student.objects.get(email=email)
#         except Student.DoesNotExist:
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

#         if student.password != password:
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

#         refresh = RefreshToken.for_user(student)
#         return Response({
#             'message': "login successful!",
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         })





































