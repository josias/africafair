from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from accounts.models import CustomUser


class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer