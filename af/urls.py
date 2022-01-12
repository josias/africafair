"""af URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, path, include
from django.views.static import serve

from django.contrib.auth.decorators import login_required
from drf_openapi3.schemas.advanced import AdvancedSchemaGenerator
from rest_framework.schemas import get_schema_view
# from af.settings.production import MEDIA_ROOT, STATIC_ROOT



urlpatterns = [

    path('my-schema/', login_required(
        get_schema_view(
            title='My API',
            description='My API description',
            version='1.0.0',
            generator_class=AdvancedSchemaGenerator,
            public=True,
        ),
        login_url='/accounts/login/',
    ), name='my_schema_name'),

    path('admin/', admin.site.urls),
    
    path('', include('fair.urls',  namespace='fair')),
    path('account/', include('drjr.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('products/', include('products.urls',  namespace='products')),
    path('fair_sites/', include('fair_sites.urls',  namespace='fair_sites')),
    path('businesses/', include('businesses.urls', namespace='businesses')),
    path('offers/', include('offers.urls',  namespace='offers'))
    #path('api-auth/', include('rest_framework.urls')),

    # Added Following Two Lines Of Code
    # re_path(r'^media/(?P<path>.*)$', serve,{'document_root': MEDIA_ROOT}), 
    # re_path(r'^static/(?P<path>.*)$', serve,{'document_root': STATIC_ROOT}), 
]
