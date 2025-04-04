from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail

from .models import CustomUser
from .serializers import RegisterSerializer, LoginSerializer, UserProfileSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

baseUrl = 'https://mizzaria.onrender.com/'

email_param = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING, format='email'),
    },
    required=['email'],
)

new_password_param = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'new_password': openapi.Schema(type=openapi.TYPE_STRING),
    },
    required=['new_password'],
)

# --- REGISTER ---
class RegisterView(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer)
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            activation_url = f"{baseUrl}api/auth/activate/{uid}/{token}/"
            send_mail(
                'Activate Your Account',
                f'Click here to activate your account: {activation_url}',
                'from@example.com',
                [user.email],
                fail_silently=False,
            )
            return Response({
                "detail": "Account created. Check your email to activate.",
                "activation_url": activation_url,
                "status": status.HTTP_201_CREATED
            }, status=status.HTTP_201_CREATED)
        return Response({
            "error": serializer.errors,
            "status": status.HTTP_400_BAD_REQUEST
        }, status=status.HTTP_400_BAD_REQUEST)


# --- ACTIVATE ACCOUNT ---
class ActivateAccountView(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            return Response({
                "error": "Invalid activation link.",
                "status": status.HTTP_400_BAD_REQUEST
            }, status=status.HTTP_400_BAD_REQUEST)

        if default_token_generator.check_token(user, token):
            if user.is_active:
                return Response({
                    "error": "Account already activated.",
                    "status": status.HTTP_400_BAD_REQUEST
                }, status=status.HTTP_400_BAD_REQUEST)

            user.is_active = True
            user.save()

            # Génération du token JWT après activation
            refresh = RefreshToken.for_user(user)
            return Response({
                "detail": "Account activated successfully.",
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "status": status.HTTP_200_OK
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "error": "Invalid or expired token.",
                "status": status.HTTP_400_BAD_REQUEST
            }, status=status.HTTP_400_BAD_REQUEST)


# --- LOGIN ---
class LoginView(APIView):
    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "status": status.HTTP_200_OK
            }, status=status.HTTP_200_OK)
        return Response({
            "error": serializer.errors,
            "status": status.HTTP_400_BAD_REQUEST
        }, status=status.HTTP_400_BAD_REQUEST)


# --- USER PROFILE ---
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


# --- LOGOUT ---
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema()
    def post(self, request):
        try:
            logout(request)
            return Response({"detail": "Logout successful.", "status": status.HTTP_200_OK}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e), "status": status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)


# --- PASSWORD RESET ---
class PasswordResetView(APIView):
    @swagger_auto_schema(request_body=email_param)
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({
                "error": "Email is required.",
                "status": status.HTTP_400_BAD_REQUEST
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_url = f"{baseUrl}api/auth/reset/{uid}/{token}/"
            send_mail(
                'Password Reset',
                f'Use this link to reset your password: {reset_url}',
                'from@example.com',
                [email],
                fail_silently=False,
            )
            return Response({
                "detail": "Reset link sent.",
                "url": reset_url,
                "status": status.HTTP_200_OK
            }, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({
                "error": "User not found.",
                "status": status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                "error": str(e),
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# --- PASSWORD RESET CONFIRM ---
class PasswordResetConfirmView(APIView):
    @swagger_auto_schema(request_body=new_password_param)
    def post(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            return Response({
                "error": "Invalid reset link.",
                "status": status.HTTP_400_BAD_REQUEST
            }, status=status.HTTP_400_BAD_REQUEST)

        if default_token_generator.check_token(user, token):
            new_password = request.data.get('new_password')
            if not new_password:
                return Response({
                    "error": "New password is required.",
                    "status": status.HTTP_400_BAD_REQUEST
                }, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(new_password)
            user.save()
            return Response({
                "detail": "Password reset successfully.",
                "status": status.HTTP_200_OK
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "error": "Invalid or expired token.",
                "status": status.HTTP_400_BAD_REQUEST
            }, status=status.HTTP_400_BAD_REQUEST)
