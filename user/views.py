# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import Student
# from .serializers import StudentSerializer, LoginSerializer
# from django.contrib.auth.hashers import check_password

# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @api_view(['GET'])
# def hello_world(request):
#     return Response({'message': 'Hello, World!'})

# class RegisterView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LoginView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data['Email']
#             password = serializer.validated_data['Password']
#             try:
#                 student = Student.objects.get(Email=email)
#                 if check_password(password, student.Password):
#                     return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
#                 else:
#                     return Response({"error": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)
#             except Student.DoesNotExist:
#                 return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer, LoginSerializer, OTPRequestSerializer, OTPVerifySerializer
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# from django.contrib.auth.models import User
# from .models import OTP

from .utils import generate_otp, send_otp_via_email


class RegisterView(APIView):
    @swagger_auto_schema(request_body=StudentSerializer)
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            try:
                student = Student.objects.get(email=email)
                if check_password(password, student.password):
                    return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)
            except Student.DoesNotExist:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class OTPRequestView(APIView):
#     @swagger_auto_schema(request_body=OTPRequestSerializer)
#     def post(self, request):
#         serializer = OTPRequestSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data['email']
#             user = Student.objects.get(email=email)
#             otp = generate_otp()
#             Student.objects.create(user=user, otp=otp)
#             send_otp_via_email(email, otp)
#             return Response({'message': 'OTP sent'}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class OTPVerifyView(APIView):
#     @swagger_auto_schema(request_body=OTPVerifySerializer)
#     def post(self, request):
#         serializer = OTPVerifySerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data['email']
#             otp = serializer.validated_data['otp']
#             user = Student.objects.get(email=email)
#             otp_instance = Student.objects.filter(user=user, otp=otp).first()
#             if otp_instance:
#                 # OTP is valid
#                 return Response({'message': 'OTP is valid'}, status=status.HTTP_200_OK)
#             else:
#                 # OTP is invalid
#                 return Response({'message': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# -----------------------
# views.py
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import OTP
from .utils import generate_otp, send_otp_via_email, get_expiration_time


class GenerateOTPView(APIView):
    def post(self, request):
        serializer = OTPRequestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'error': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
            
            otp = generate_otp()
            expiration_time = get_expiration_time()
            OTP.objects.create(user=user, otp=otp, expires_at=expiration_time)
            send_otp_via_email(email, otp)
            
            return Response({'message': 'OTP sent'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import OTP


class VerifyOTPView(APIView):
    def post(self, request):
        serializer = OTPVerifySerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp_provided = serializer.validated_data['otp']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'error': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
            
            try:
                otp_record = OTP.objects.get(user=user, otp=otp_provided)
            except OTP.DoesNotExist:
                return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
            
            if not otp_record.is_valid():
                return Response({'error': 'OTP expired'}, status=status.HTTP_400_BAD_REQUEST)
            
            # OTP is valid and not expired
            return Response({'message': 'OTP verified'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

