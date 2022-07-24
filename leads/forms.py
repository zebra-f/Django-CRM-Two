from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField

from .models import Lead, User, Agent


class LeadModelForm(forms.ModelForm):
    # agent = forms.ModelChoiceField(queryset=Agent.objects.all())

    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'phone',
            'email',
            'source',
            'agent',
        )

    # def __init__(self, *args, **kwargs):
    #     initial = kwargs['initial']
    #     agents = Agent.objects.filter(affiliation=initial['user'].user.affiliation)
    #     super().__init__(*args, **kwargs)
    #     self.fields["agent"].queryset = agents
        


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = (
            'username',
        )
        field_classes = {'username': UsernameField}


class AssignAgentForm(forms.ModelForm):

    class Meta:
        model = Lead
        fields = (
            'agent',
        )

    # forms.Form
    # agent = forms.ModelChoiceField(queryset=None)

    # def __init__(self, *args, **kwargs):
    #     initial = kwargs['initial']
    #     agents = Agent.objects.filter(affiliation=initial['user'].affiliation)
    #     super().__init__(*args, **kwargs)
    #     self.fields["agent"].queryset = agents

    # forms.Model


class DeleteForm(forms.Form):
    pass
