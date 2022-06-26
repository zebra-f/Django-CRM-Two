from django.urls import path, include

from .views import home_page


# required for the `namespace` keyword arguemtn in crm.urls
app_name = 'landing'

urlpatterns = [
    path('', home_page, name='home-page'),
]