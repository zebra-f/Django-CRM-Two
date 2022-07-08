from django.urls import path

from .views import (
    LeadListView,
    LeadDetailView, 
    LeadCreateView, 
    LeadUpdateView,
    LeadAssignAgentUpdateView ,
    lead_delete,
    )


# required for the `namespace` keyword arguemtn in crm.urls
app_name = 'leads'

urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/update/assignagent', LeadAssignAgentUpdateView.as_view(), name='lead-assign-agent-update'),
    path('<int:pk>/delete/', lead_delete, name='lead-delete'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
    # path('create/', lead_create, name='lead-create'),
]
