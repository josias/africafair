from django.urls import path
from businesses.api import views

app_name = 'businesses'
urlpatterns = [
    path('signages/', views.BusinessListCreateView.as_view(), name='businesses-list'),
    path('signages/<int:pk>/', views.BusinessRetrieveUpdateDestroyView.as_view(), name='businesses-detail'),
    path('shops/', views.ShopListCreateView.as_view(), name='shop-list'),
    path('shops/<int:pk>/', views.ShopRetrieveUpdateDestroyView.as_view(), name='shop-detail'),
]
