from rest_framework import generics
from businesses.api import serializers
from businesses.models import Shop, Business


class BusinessListCreateView(generics.ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = serializers.BusinessSerializer
    permission_classes = []


class BusinessRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Business.objects.all()
    serializer_class = serializers.BusinessSerializer
    permission_classes = []


class ShopListCreateView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = serializers.ShopSerializer
    permission_classes = []


class ShopRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = serializers.ShopSerializer
    permission_classes = []

