from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from businesses.models import Business, Shop
from af.settings.base import AUTH_USER_MODEL
from accounts.models import CustomUser

class BusinessAdmin(GuardedModelAdmin):
    model = Business

admin.site.register(Business, BusinessAdmin)


admin.site.register(Shop)