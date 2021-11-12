from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views

from accounts.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, LoginView, LogoutView, ProfileView, SignUpView, VisitorSignUpView #, CustomerSignUpView, SellerSignUpView, OwnerSignUpView, EditorSignUpView
from accounts.api.views import UserList, UserDetail


app_name = 'accounts'
urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
    path('api/users/', UserList.as_view(), name='users_list'),
    path('api/users/<int:pk>/', UserDetail.as_view(), name='users_detail'),

    
    path('login/', LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/', PasswordChangeView.as_view(),name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetConfirmView.as_view(), name='password_reset_complete'),
    path('signin/', LoginView.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), name='signout'),
    path('profile/',ProfileView.as_view(), name='profile'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/visitor/', VisitorSignUpView.as_view(), name='visitor_signup'),
   # path('signup/customer/', CustomerSignUpView.as_view(), name='customer_signup'),
   # path('signup/seller/', SellerSignUpView.as_view(), name='seller_signup'),
   # path('signup/owner/', OwnerSignUpView.as_view(), name='owner_signup'),
   # path('signup/editor/', EditorSignUpView.as_view(), name='editor_signup'),
]