from django import forms
from django.contrib.auth import get_user_model

from .models import Agent


User = get_user_model()


class UserAgentModelForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
        )


class AgentModelForm(forms.ModelForm):

    class Meta:
        model = Agent
        fields = (
            'user',
        )


class AgentUpdateModelForm(forms.ModelForm):

    class Meta:
        model = Agent
        fields = (
            'user',
            'affiliation'
        )

