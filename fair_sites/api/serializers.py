from rest_framework import serializers
from businesses.api.serializers import ShopSerializer
from fair_sites.models import Site, Quarter, Zone, Town, Department, Country


class SiteSerializer(serializers.ModelSerializer):
    shops = ShopSerializer(many=True, read_only=True)

    class Meta:
        model = Site
        fields = [
            'street',
            'address',
            'shops',
        ] 

class QuaterSerializer(serializers.ModelSerializer):
    sites = SiteSerializer(many=True, read_only=True)

    class Meta:
        model = Quarter
        fields = [
            'name', 
            'sites',
        ]


class ZoneSerializer(serializers.ModelSerializer):
    quaters = QuaterSerializer(many=True, read_only=True)

    class Meta:
        model = Zone
        fields = [
            'name', 
            'quaters',
        ]


class TownSerializer(serializers.ModelSerializer):
    zones = ZoneSerializer(many=True, read_only=True)

    class Meta:
        model = Quarter
        fields = [
            'name', 
            'zones',
        ]


class DepartmentSerializer(serializers.ModelSerializer):
    towns = TownSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = [
            'name',
            'towns',
        ]


class CountrySerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = [
            'name',
            'departments'
        ]
