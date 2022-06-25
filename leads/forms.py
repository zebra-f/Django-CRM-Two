from django import forms

from .models import Lead, User, Agent


# class LeadForm(forms.Form):
    
#     SOURCE_CHOICES = (
#         ('Youtube', 'Youtube'),
#         ('Google', 'Google'),
#         ('Facebook', 'Facebook'),
#         ('Newsletter', 'Newsletter'),
#         ('Other', 'Other'),
#     )

#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     age = forms.IntegerField(min_value=18, max_value=120)

#     source = forms.ChoiceField(choices=SOURCE_CHOICES)

class LeadModelForm(forms.ModelForm):

    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'source',
            'agent'
        )
