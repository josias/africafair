from django.db import models
from django.utils.translation import gettext_lazy as _
from af.settings.base import AUTH_USER_MODEL
from af.core.models import TimestampModel
from products.models import Product
from businesses.models import Shop


class Package(TimestampModel):
    #TODO Manage Products Category
    name = models.CharField(verbose_name=_('name'), max_length=100)
    products = models.ManyToManyField(Product, related_name='packages')
    price = models.FloatField(verbose_name=_('price'))
    retailer = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE, 
        related_name='packages'
    )
    customers = models.ManyToManyField(
        AUTH_USER_MODEL,  
        through='Purchase',
    )
    is_on_fair = models.BooleanField(_('is on fair'), default=True)
    is_published = models.BooleanField(verbose_name=_('is published'), default=False)
    publicity_duration = models.DurationField(_('publicity duration'))
    

    def Publish(self, **kwargs):
        self.publicity_duration = kwargs['duration']
        self.is_on_fair = True
        self.is_published = True
        return self.is_published

    def OptOutFair(self):
        self.is_on_fair = False
        return self.is_on_fair

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _('package')
        verbose_name_plural = _('packages')


class Bonus(TimestampModel):
    pass


class Purchase(TimestampModel):
    package = models.ForeignKey(
        Package,
        verbose_name=_('packages'),
        on_delete=models.CASCADE,
        related_name='purchases'
    )
    customer = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'is_active':True, 'groups__name':'customer'},
        related_name='purchases'
    )
    quantity= models.FloatField(verbose_name=_('quantity'))
    
    @property
    def amount(self):
        amount = self.quantity * self.package.price
        return amount

    @property
    def discount(self):
        return self.amount * self.package.retailler__bonus_rate
