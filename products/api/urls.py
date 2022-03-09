from django.urls import path
from products.api.views import products_list, products_details, ProductList, ProductDetail


urlpatterns = [
    path('list/', ProductList.as_view(), name='products_list'),
    path('<int:pk>', ProductDetail.as_view(), name='products_detail'),
]