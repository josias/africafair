from django.contrib.auth import login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect, resolve_url, reverse

from django.views.generic import CreateView
from django.views.generic.base import TemplateView, RedirectView

from accounts.models import CustomUser
from accounts.forms import CustomLoginForm, CustomPasswordChangeForm, VisitorSignUpForm



class LoginView(auth_views.LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomLoginForm

    def get_success_url(self):
        return resolve_url('accounts:login')
    
    def get_success_url_allowed_hosts(self):
        return super().get_success_url_allowed_hosts()


class LogoutView(auth_views.LogoutView):
    """
    A view that logout user and redirect to homepage.
    """
    template_name = 'registration/logout.html'
    permanent = False
    query_string = True
    pattern_name = 'fair:index'

    def get_redirect_url(self, *args, **kwargs):
        """
        Logout user and redirect to target url.
        """
        if self.request.user.is_authenticated():
            logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)


class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'registration/password_change.html'
    form_class = CustomPasswordChangeForm
    success_url = 'accounts:password_change_done'


class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'


class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'registration/password_change.html'
    success_url = 'accounts:password_reset_done'


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'
    success_url = 'accounts:password_reset_confirm'


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = 'accounts:password_reset_complete'

class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'  


class SignUpView(TemplateView):
    template_name = 'accounts/signup.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'


class VisitorSignUpView(CreateView):
    model = CustomUser
    form_class = VisitorSignUpForm
    template_name = 'accounts/visitor_signup_form.html'

    def get_context_data(self, **kwargs):  
        kwargs['user_type'] = 'visitor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('fair:home')