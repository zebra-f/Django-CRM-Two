from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField

from .models import Lead, User, Agent


class LeadModelForm(forms.ModelForm):
    
    agent = forms.ModelChoiceField(queryset=None)

    class Meta:

        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'source',
        )

    def __init__(self, *args, **kwargs):
        initial = kwargs['initial']
        agents = Agent.objects.filter(affiliation=initial['user'].user.affiliation)

        super().__init__(*args, **kwargs)

        self.fields["agent"].queryset = agents
        


class CustomUserCreationForm(UserCreationForm):

    class Meta:

        model = User
        fields = (
            'username',
        )
        field_classes = {'username': UsernameField}