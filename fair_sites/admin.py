from django.contrib import admin
from fair_sites.models import Site, Quarter, Zone, Town, Department, Country

admin.site.register(Country)
admin.site.register(Department)
admin.site.register(Town)
admin.site.register(Zone)
admin.site.register(Quarter)
admin.site.register(Site)