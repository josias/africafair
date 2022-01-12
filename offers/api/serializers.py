from rest_framework import serializers
from products.api.serializers import ProductSerializer
from businesses.api.serializers import ShopSerializer

from offers.models import Package, Purchase
from products.models import Product
from af.settings.base import AUTH_USER_MODEL


class CustomSerializer(serializers.HyperlinkedModelSerializer):

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(CustomSerializer, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields


class PurchaseSerializer(CustomSerializer):

    class Meta:
        model = Purchase
        fields = '__all__'


class PackageSerializer(CustomSerializer):
    
    class Meta:
        model = Package
        fields = '__all__'
        extra_fields = ['purchases']

