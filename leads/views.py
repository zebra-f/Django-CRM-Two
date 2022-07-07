from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import (
    TemplateView, ListView, DeleteView, DetailView, RedirectView, CreateView, UpdateView
    )
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Lead, Agent, User
from .forms import LeadModelForm, CustomUserCreationForm

# Create your views here.

# Registration

class SignupView(CreateView):
    
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('leads:lead-list'))
        else:
            return super().get(request, *args, **kwargs)


# Leads

class LeadListView(LoginRequiredMixin, ListView):

    template_name = 'leads/lead_list.html'
    model = Lead
    context_object_name = 'leads'

    def get_queryset(self):
        
        user = self.request.user
        
        queryset = Lead.objects.filter(affiliation=user.affiliation)

        if user.is_agent:
            queryset = queryset.filter(agent=user.agent)
        
        return queryset
    

class LeadDetailView(LoginRequiredMixin, DetailView):

    template_name = 'leads/lead_detail.html'
    model = Lead
    context_object_name = 'lead'


class LeadCreateView(LoginRequiredMixin, CreateView):

    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm
    success_url = reverse_lazy('leads:lead-list')


    def get_initial(self):
        self.initial['user'] = self.request.user.affiliation 
        # self.initial['first_name'] = "John"
        return super().get_initial()


    def form_valid(self, form):
        lead = form.save(commit=False)
        lead.affiliation = self.request.user.affiliation
        lead.save()

        return HttpResponseRedirect(self.success_url)


class LeadUpdateView(LoginRequiredMixin, UpdateView):
    
    template_name = 'leads/lead_update.html'
    model = Lead
    form_class = LeadModelForm
    success_url = reverse_lazy('leads:lead-list')


def lead_delete(request, pk):

    lead = Lead.objects.get(id=pk)
    lead.delete()

    return redirect('/leads')







