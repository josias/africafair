from django.shortcuts import render
from django.contrib.auth import logout
from django.views.generic.base import TemplateView, RedirectView

def error_404(request, exception):

        return render(request,'404.html')

# def error_500(request,  exception):
#        return render(request,'500.html', data)
        
def error_403(request, exception):

        return render(request,'403.html')

# def error_400(request,  exception):
#        return render(request,'400.html', data) 


class IndexView(TemplateView):
    template_name = 'fair/index.html'


class HomeView(TemplateView):
    template_name = 'fair/home.html'


class AboutView(TemplateView):
    template_name = 'fair/about.html'
