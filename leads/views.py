from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import (
    TemplateView, ListView, DeleteView, DetailView, RedirectView, CreateView, UpdateView
    )
from django.contrib.auth.mixins import LoginRequiredMixin

from django import forms


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
        
        if user.is_owner:
            queryset = Lead.objects.filter(affiliation=user.affiliation)
        elif user.is_agent:
            queryset = Lead.objects.filter(affiliation=user.agent.affiliation)
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
        # if self.request.user.is_owner:
        #     self.initial['user'] = self.request.user.affiliation 
        # self.initial['first_name'] = "John"
        return super().get_initial()


    def get_form(self, form_class=None):
        """Return an instance of the form to be used in this view."""
        if form_class is None:
            form_class = self.get_form_class()
        
        if self.request.user.is_owner:
            form_class.base_fields['agent'] = forms.ModelChoiceField(
                queryset=Agent.objects.filter(affiliation=self.request.user.affiliation))  
        # `form_valid` method will handle `agent` field
        elif self.request.user.is_agent and self.request.method == 'GET':
            del form_class.base_fields['agent'] 
        
        return form_class(**self.get_form_kwargs())


    def form_valid(self, form):
        lead = form.save(commit=False)
        
        if self.request.user.is_owner:
            lead.affiliation = self.request.user.affiliation
        elif self.request.user.is_agent:
            lead.affiliation = self.request.user.agent.affiliation
        
        if self.request.user.is_agent:
            lead.agent = self.request.user.agent

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







