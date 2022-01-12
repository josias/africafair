from django.urls import path, include
from rest_framework.routers import DefaultRouter
from fair_sites.api import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'countries', views.CountryViewSet)
router.register(r'departments', views.DepartmentViewSet)
router.register(r'towns', views.TownViewSet)
router.register(r'zones', views.ZoneViewSet)
router.register(r'quaters', views.QuarterViewSet)
router.register(r'sites', views.SiteViewSet)

app_name = 'fair_sites'
# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]