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

# def lead_create(request):

#     if request.method == 'POST':
#         # ModelForm
#         form = LeadModelForm(request.POST)
        
#         if form.is_valid():
#             # form.cleaned_data returns a dictionary
#             # Lead.objects.create(**form.cleaned_data)
#             form.save()       

#             return redirect('/leads')

#     form = LeadModelForm()

#     context = {
#         "form": form
#     }

#     return render(request, 'leads/lead_create.html', context)

class LeadUpdateView(UpdateView):
    template_name = 'leads/lead_update.html'
    model = Lead
    form_class = LeadModelForm
    success_url = reverse_lazy('leads:lead-list')


# def lead_update(request, pk):
     
#     lead = Lead.objects.get(id=pk)

#     if request.method == 'POST':
#         form = LeadModelForm(request.POST)
        
#         if form.is_valid():
#             form.save()

#             return redirect('/leads')

#     form = LeadModelForm(instance=lead)
    
#     context = {
#         "lead": lead,
#         "form": form
#     }

#     return render(request, 'leads/lead_update.html', context)


def lead_delete(request, pk):

    lead = Lead.objects.get(id=pk)
    lead.delete()

    return redirect('/leads')




