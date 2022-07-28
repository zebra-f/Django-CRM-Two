from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import (
    TemplateView,
    ListView, 
    DeleteView, 
    DetailView, 
    RedirectView, 
    CreateView, 
    UpdateView,
    FormView
    )
from django.contrib.auth.mixins import LoginRequiredMixin

from django import forms


from .models import Lead
from .forms import LeadModelForm, AssignAgentForm, DeleteForm
from .filters import LeadListFilter
from .mixins import OwnerRequiredMixin, LeadsManagementAccessPermissionMixin

from agents.models import Agent

# Create your views here.

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


    def render_to_response(self, context, **response_kwargs):
        response_kwargs.setdefault('content_type', self.content_type)
        
        if len(self.request.GET) > 0:
            filter = LeadListFilter(self.request.GET, queryset=self.model.objects.all())
            context_update = {
                'filter': filter,
                self.context_object_name: filter.qs
            }
            context.update(**context_update)
       
        else:
            context.update(
                filter=LeadListFilter(),
            )

        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            using=self.template_engine,
            **response_kwargs
        )
    

class LeadDetailView(
    LoginRequiredMixin,
    LeadsManagementAccessPermissionMixin, 
    DetailView):

    template_name = 'leads/lead_detail.html'
    model = Lead
    context_object_name = 'lead'


class LeadCreateView(LoginRequiredMixin, CreateView):

    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm
    success_url = reverse_lazy('leads:lead-list')


    # def get_initial(self):
    #     # self.initial['first_name'] = "John"
    #     return super().get_initial()


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


class LeadUpdateView(
    LoginRequiredMixin,
    LeadsManagementAccessPermissionMixin, 
    UpdateView
    ):
    
    template_name = 'leads/lead_update.html'
    model = Lead
    form_class = LeadModelForm
    success_url = reverse_lazy('leads:lead-list')


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


class LeadAssignAgentUpdateView(
    OwnerRequiredMixin,
    LeadsManagementAccessPermissionMixin, 
    LoginRequiredMixin, 
    UpdateView
    ):

    template_name = 'leads/lead_assign_agent_update.html'
    model = Lead
    form_class = AssignAgentForm
    success_url = reverse_lazy('leads:lead-list')


    def get_form(self, form_class=None):
        """Return an instance of the form to be used in this view."""
        if form_class is None:
            form_class = self.get_form_class()

        form_class.base_fields['agent'] = forms.ModelChoiceField(
            queryset=Agent.objects.filter(affiliation=self.request.user.affiliation))  

        return form_class(**self.get_form_kwargs())
    
    
    # FormView
    # def get_form_kwargs(self):
    #     """Return the keyword arguments for instantiating the form."""
    #     kwargs = super().get_form_kwargs()
    #     if hasattr(self, 'object'):
    #         kwargs.update({'instance': self.object})
    #     kwargs['initial']['user'] = self.request.user
        
    #     return kwargs



def lead_delete(request, pk):

    if request.method == "GET":
        return HttpResponse("What are you doing here?!")
    
    if request.method == "POST":
        
        form = DeleteForm(request.POST)
        if form.is_valid:
            lead = Lead.objects.get(pk=pk)
            
            if request.user.is_agent:
                if request.user.agent == lead.agent:
                    lead.delete()
            
            elif request.user.is_owner:
                if lead.affiliation == request.user.affiliation:
                    lead.delete()

    return redirect('/leads')







