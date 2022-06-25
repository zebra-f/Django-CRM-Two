from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Lead, Agent, User
from .forms import LeadModelForm

# Create your views here.

def lead_list(request):

    leads = Lead.objects.all()
    
    context = {
        "name": "Joe",
        "age": 45,
        "leads": leads
    }

    return render(request, 'leads/lead_list.html', context)


def lead_detail(request, pk):

    lead = Lead.objects.get(id=pk)

    context = {
        "lead": lead
    }

    return render(request, 'leads/lead_detail.html', context)


def lead_create(request):

    if request.method == 'POST':
        # ModelForm
        form = LeadModelForm(request.POST)
        
        if form.is_valid():
            # form.cleaned_data returns a dictionary
            # Lead.objects.create(**form.cleaned_data)
            form.save()       

            return redirect('/leads')

    form = LeadModelForm()

    context = {
        "form": form
    }

    return render(request, 'leads/lead_create.html', context)


def lead_update(request, pk):
     
    lead = Lead.objects.get(id=pk)

    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance=lead)
        
        if form.is_valid():
            form.save()

            return redirect('/leads')

    form = LeadModelForm(instance=lead)
    
    context = {
        "lead": lead,
        "form": form
    }

    return render(request, 'leads/lead_update.html', context)


def lead_delete(request, pk):

    lead = Lead.objects.get(id=pk)
    lead.delete()

    return redirect('/leads')




