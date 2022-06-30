from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import (
    TemplateView, ListView, DeleteView, DetailView, RedirectView, CreateView, UpdateView
    )
from django.contrib.auth.mixins import LoginRequiredMixin

from leads.models import Lead, Agent

# Create your views here.

# Registration


# Agents

class AgentListView(LoginRequiredMixin, ListView):

    template_name: str = 'agents/agent_list.html'
    model = Agent
    context_object_name = 'agents'
    

class AgentDetailView(LoginRequiredMixin, DetailView):

    template_name = 'agents/agent_detail.html'
    model = Agent
    context_object_name = 'agent'


class AgentCreateView(LoginRequiredMixin, CreateView):

    template_name = 'agents/agent_create.html'
    form_class = None
    success_url = reverse_lazy('agents:agent-list')


class AgentUpdateView(LoginRequiredMixin, UpdateView):
    
    template_name = 'agent/agen_update.html'
    model = Agent
    form_class = None
    success_url = reverse_lazy('agents:agent-list')


def agent_delete(request, pk):

    lead = Lead.objects.get(id=pk)
    lead.delete()

    return redirect('/agents')