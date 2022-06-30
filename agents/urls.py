from django.urls import path

from .views import (
    AgentListView,
    AgentDetailView, 
    AgentCreateView, 
    AgentUpdateView, 
    agent_delete,
    )


# required for the `namespace` keyword arguemtn in crm.urls
app_name = 'agents'

urlpatterns = [
    path('', AgentListView.as_view(), name='agent-list'),
    path('<int:pk>/', AgentDetailView.as_view(), name='agent-detail'),
    path('create/', AgentCreateView.as_view(), name='agent-create'),
    path('<int:pk>/update/', AgentUpdateView.as_view(), name='agent-update'),
    path('<int:pk>/delete/', agent_delete, name='agent-delete'),
]