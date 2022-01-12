from django.urls import path, include
from rest_framework.routers import DefaultRouter
from offers.api import views 

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'packages', views.PackageViewSet)
router.register(r'purchases', views.PurchaseViewSet)

app_name = 'offers'
# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]