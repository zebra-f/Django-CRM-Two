from django.shortcuts import render, redirect  
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.views.generic import (
    TemplateView, ListView, DeleteView, DetailView, RedirectView, CreateView, UpdateView
    )

from .models import Lead, Agent, User
from .forms import LeadModelForm

# Create your views here.

class LeadListView(ListView):

    template_name: str = 'leads/lead_list.html'
    model = Lead
    context_object_name = 'leads'
    

class LeadDetailView(DetailView):

    template_name = 'leads/lead_detail.html'
    model = Lead
    context_object_name = 'lead'


class LeadCreateView(CreateView):

    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm
    success_url = reverse_lazy('leads:lead-list')


class LeadUpdateView(UpdateView):
    
    template_name = 'leads/lead_update.html'
    model = Lead
    form_class = LeadModelForm
    success_url = reverse_lazy('leads:lead-list')


def lead_delete(request, pk):

    lead = Lead.objects.get(id=pk)
    lead.delete()

    return redirect('/leads')




