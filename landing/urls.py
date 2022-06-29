from django.urls import path
from django.views.generic import TemplateView


# required for the `namespace` keyword arguemtn in crm.urls
app_name = 'landing'

urlpatterns = [
    path('', TemplateView.as_view(template_name="landing/home_page.html"), name='home-page'),
    
]