from rest_framework import viewsets
from offers.api.serializers import PurchaseSerializer, PackageSerializer
from offers.models import Package, Purchase


class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = []


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = []
