from django import forms
from leads.models import Agent


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

