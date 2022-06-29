from django.urls import path
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    )


# required for the `namespace` keyword arguemtn in crm.urls
app_name = 'landing'

urlpatterns = [
    path('', TemplateView.as_view(template_name="landing/home_page.html"), name='home-page'),
    path('login/', LoginView.as_view(
        template_name="landing/registration/login.html",
        next_page=reverse_lazy("leads:lead-list"),
        redirect_authenticated_user=True,
        ), name='login'),
    path('logout/', LogoutView.as_view(
        next_page=reverse_lazy("landing:home-page")
        ), name='logout'),

    
]