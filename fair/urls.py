from django.urls import include, path
from fair.views import IndexView, HomeView, AboutView

"""
handler404 = 'fair.views.error_404'
handler500 = 'fair.views.error_500'
handler403 = 'fair.views.error_403'
handler400 = 'fair.views.error_400'
"""

app_name = 'fair'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('home/', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    
]
