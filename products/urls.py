from django.urls import path, include
from products.views import products_list, products_details
from products.api.views import ProductList, ProductDetail

app_name = 'produts'
urlpatterns = [
    path('list/', products_list, name='products_list'),
    path('<int:pk>', products_details, name='products_detail'),
    path('api/list/', ProductList.as_view(), name='products_api_list'),
    path('api/<int:pk>', ProductDetail.as_view(), name='products_api_detail'),
  
]