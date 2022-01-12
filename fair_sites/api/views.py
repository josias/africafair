from rest_framework import viewsets, permissions
from fair_sites.api import serializers
from fair_sites.models import Site, Quarter, Zone, Town, Department, Country


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = serializers.CountrySerializer
    permission_classes = []


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    permission_classes = []


class TownViewSet(viewsets.ModelViewSet):
    queryset = Town.objects.all()
    serializer_class = serializers.TownSerializer
    permission_classes = []


class ZoneViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = serializers.ZoneSerializer
    permission_classes = []


class QuarterViewSet(viewsets.ModelViewSet):
    queryset = Quarter.objects.all()
    serializer_class = serializers.QuaterSerializer
    permission_classes = []


class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = serializers.SiteSerializer
    permission_classes = []



