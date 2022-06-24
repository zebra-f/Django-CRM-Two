from django.urls import path

from .views import lead_list, lead_detail


# required for the `namespace` keyword arguemtn in crm.urls
app_name = 'leads'

urlpatterns = [
    path('', lead_list, name='lead_list'),
    path('<int:pk>/', lead_detail, name='lead_detail')
]
