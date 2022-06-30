"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    )

from leads.views import SignupView


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # authentication
    path('login/', LoginView.as_view(
        next_page=reverse_lazy("leads:lead-list"),
        redirect_authenticated_user=True,
        ), name='login'),
    path('logout/', LogoutView.as_view(
        next_page=reverse_lazy("landing:home-page")
        ), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),

    # apps
    path('', include('landing.urls', namespace='landing')),
    path('leads/', include('leads.urls', namespace='leads')),
    path('agents/',include('agents.urls', namespace='agents')),

    # static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
