from rest_framework import serializers
from accounts.api.serializers import CustomUserSerializer
from versatileimagefield.serializers import VersatileImageFieldSerializer
from businesses.models import Business, Shop


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = [
            'short_name',
            'is_headquater',
            'whatsapp',
            'bonus_rate'
        ]          


class BusinessSerializer(serializers.ModelSerializer): 
    logo = VersatileImageFieldSerializer(
        sizes= 'logo'
    )
    point_of_sales = ShopSerializer(many=True, read_only=True)

    class Meta: 
        model = Business 
        fields = [
            'full_name', 
            'logo',
            'point_of_sales'   
        ]