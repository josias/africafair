from lib2to3.pgen2.tokenize import TokenError
import jwt
from django.conf import settings
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.exceptions import ValidationError
from rest_framework import  serializers

from accounts.models import CustomUser, UserProfile

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email')

class CustomUserDRJRSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email', 'password')
        
class UserProfileSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:userprofile-detail")
    user = CustomUserSerializer(many=False, read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=4, max_length=128, write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "password", "email", "is_active"]

    def create(self, validated_data):

        try:
            CustomUser.objects.get(email=validated_data["email"])
        except ObjectDoesNotExist:
            return CustomUser.objects.create_user(**validated_data)

        raise ValidationError({"success": False, "msg": "Email already taken"})


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs 

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('Bad token')



""" from datetime import datetime, timedelta

def _generate_jwt_token(user):
    token = jwt.encode(
        {"id": user.pk, "exp": datetime.utcnow() + timedelta(days=7)},
        settings.SECRET_KEY,
    )

    return token


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)

        if email is None:

            raise exceptions.ValidationError(
                {"success": False, "msg": "Email is required to login"}
            )
        if password is None:
            raise exceptions.ValidationError(
                {"success": False, "msg": "Password is required to log in."}
            )
        user = authenticate(username=email, password=password)

        if user is None:
            raise exceptions.AuthenticationFailed({"success": False, "msg": "Wrong credentials"})

        if not user.is_active:
            raise exceptions.ValidationError(
                {"success": False, "msg": "User is not active"}
            )

        try:
            session = ActiveSession.objects.get(user=user)
            if not session.token:
                raise ValueError

            jwt.decode(session.token, settings.SECRET_KEY, algorithms=["HS256"])

        except (ObjectDoesNotExist, ValueError, jwt.ExpiredSignatureError):
            session = ActiveSession.objects.create(
                user=user, token=_generate_jwt_token(user)
            )

        return {
            "success": True,
            "token": session.token,
            "user": {"_id": user.pk, "username": user.username, "email": user.email},
        }
        

class RegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            "name",
            "Email_Address",
            "zipcode",
            "Date_of_Birth",
            "password",

        ]

        extra_kwargs = {"password": {"write_only": True}}
        password = self.validated_data["password"]
        account.set_password(password)
        account.save()
        return account        
        
         """