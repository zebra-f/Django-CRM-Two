from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import HttpResponseRedirect

from .forms import CustomUserCreationForm

# Create your views here. 

# Registration

class SignupView(CreateView):
    
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('leads:lead-list'))
        else:
            return super().get(request, *args, **kwargs)



