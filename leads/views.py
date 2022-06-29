from django.shortcuts import render, redirect  
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (
    TemplateView, ListView, DeleteView, DetailView, RedirectView, CreateView, UpdateView
    )
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Lead, Agent, User
from .forms import LeadModelForm, CustomuserCreationForm

# Create your views here.

# Registration

class SignupView(CreateView):
    
    template_name = 'registration/signup.html'
    form_class = CustomuserCreationForm
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('leads:lead-list')
        else:
            return super().get(request, *args, **kwargs)


# Leads

class LeadListView(LoginRequiredMixin, ListView):

    template_name: str = 'leads/lead_list.html'
    model = Lead
    context_object_name = 'leads'
    

class LeadDetailView(LoginRequiredMixin, DetailView):

    template_name = 'leads/lead_detail.html'
    model = Lead
    context_object_name = 'lead'


class LeadCreateView(LoginRequiredMixin, CreateView):

    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm
    success_url = reverse_lazy('leads:lead-list')


class LeadUpdateView(LoginRequiredMixin, UpdateView):
    
    template_name = 'leads/lead_update.html'
    model = Lead
    form_class = LeadModelForm
    success_url = reverse_lazy('leads:lead-list')


def lead_delete(request, pk):

    lead = Lead.objects.get(id=pk)
    lead.delete()

    return redirect('/leads')







