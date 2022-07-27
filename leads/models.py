from django.db import models

from agents.models import Agent
from landing.models import Affiliation

# Create your models here.

class Lead(models.Model):

    SOURCE_CHOICES = (
        ('Youtube', 'Youtube'),
        ('Google', 'Google'),
        ('Facebook', 'Facebook'),
        ('Newsletter', 'Newsletter'),
        ('Other', 'Other'),
    )   

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField(default=0, null=True, blank=True)
    
    # contact
    email = models.CharField(max_length=40, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    source = models.CharField(max_length=100, choices=SOURCE_CHOICES)

    # on_delete=models.CASCADE
    # on_delete=models.SET_DEFAULT, default='name'
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True)
    affiliation = models.ForeignKey(Affiliation, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class LeadStatus(models.Model):
    
    STATUS_CHOICES = (
        ('New', 'New'),
        ('Open', 'Open'),
        ('Qualified', 'Qualified'),
        ('Contacted', 'Contacted'),
        ('Conversion', 'Conversion'),
        ('Converted', 'Converted'),
    ) 

    lead = models.OneToOneField("Lead", on_delete=models.CASCADE)

    status = models.CharField(max_length=40, default="New",  choices=STATUS_CHOICES)
    last_status_update = models.DateTimeField(auto_now_add=True, null=False)
    
    public_note = models.CharField(max_length=1000, null=True, blank=True)
    private_note = models.CharField(max_length=1000, null=True, blank=True)