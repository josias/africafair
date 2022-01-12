from re import I
from django.db import models
from django.utils.translation import gettext_lazy as _
from treebeard.mp_tree import MP_Node
from versatileimagefield.fields import VersatileImageField, PPOIField

from af.core.models import TimestampModel
from af.settings.base import AUTH_USER_MODEL
from businesses.models import Business


class Category(MP_Node):
    name = models.CharField(max_length=30)
    node_order_by = ['name']

    def __str__(self):
        return 'Category: {}'.format(self.name)


class Product(TimestampModel):
    name = models.CharField(verbose_name=_('name'), max_length=50)
    description = models.CharField(verbose_name=_('description'), max_length=200,)
    category = models.ForeignKey(Category, verbose_name=_('product category'), related_name='products', default='not-classified', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    business = models.ForeignKey(Business, verbose_name=_('business'), null=True, blank=True, related_name='products', on_delete=models.CASCADE)
    picture = VersatileImageField(
        'product',
        upload_to='static/assets/img/products_pictures/',
        ppoi_field='picture_ppoi', 
        blank=True, 
        null=True,
    )
    class Meta:
        ordering = ['name']

    # Methods
    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        return self.name
