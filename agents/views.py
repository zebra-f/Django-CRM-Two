from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import (
    TemplateView, ListView, DeleteView, DetailView, RedirectView, CreateView, UpdateView
    )
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail

from leads.models import Agent
from .forms import AgentUpdateModelForm, UserAgentModelForm
from .mixins import OwnerRequiredMixin


# Create your views here.

# Agents

class AgentListView(LoginRequiredMixin, OwnerRequiredMixin, ListView):

    template_name: str = 'agents/agent_list.html'
    model = Agent
    context_object_name = 'agents'


    def get_queryset(self):
        
        # TODO
        # use this for other methods

        affiliation = self.request.user.affiliation
        
        return Agent.objects.filter(affiliation=affiliation)

    

class AgentDetailView(LoginRequiredMixin, OwnerRequiredMixin, DetailView):

    template_name = 'agents/agent_detail.html'
    model = Agent
    context_object_name = 'agent'


class AgentCreateView(LoginRequiredMixin, OwnerRequiredMixin, CreateView):

    template_name = 'agents/agent_create.html'
    form_class = UserAgentModelForm
    success_url = reverse_lazy('agents:agent-list')

    def form_valid(self, form):
        
        user = form.save(commit=False)
        user.is_owner = False
        user.is_agent = True
        # TODO
        # randomize password
        user.set_password("password1234")
        user.save()
        
        Agent.objects.create(
            user=user,
            affiliation = self.request.user.affiliation
        )

        send_mail(
            subject="Agent Invitation",
            message="You were added as an Agent. Please login",
            from_email="test@test.com",
            recipient_list=[
                user.email
            ]
        )

        return HttpResponseRedirect(self.success_url)


class AgentUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    
    template_name = 'agents/agent_update.html'
    model = Agent
    form_class = AgentUpdateModelForm
    success_url = reverse_lazy('agents:agent-list')


def agent_delete(request, pk):

    agent = Agent.objects.get(id=pk)
    agent.delete()

    return redirect('/agents')


