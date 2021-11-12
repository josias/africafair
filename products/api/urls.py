from django.urls import path
from products.api.views import products_list, products_details


urlpatterns = [
    path('list/', products_list, name='products_list'),
    path('<int:pk>', products_details, name='products_detail'),
]