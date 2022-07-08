from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


# Create your models here.

class User(AbstractUser):
    is_owner = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class Affiliation(models.Model):
    name = models.CharField(max_length=200, null=True)
    user = models.OneToOneField("User", on_delete=models.CASCADE)

    def __str__(self):
        if self.name:
            return f"{self.user.username}, {self.name}"
        else:
            return self.user.username


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
    agent = models.ForeignKey("Agent", on_delete=models.SET_NULL, null=True)
    affiliation = models.ForeignKey("Affiliation", on_delete=models.CASCADE)

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


class Agent(models.Model):

    user = models.OneToOneField("User", on_delete=models.CASCADE)
    affiliation = models.ForeignKey("Affiliation", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"


# Signals 

def post_user_created_singal(sender, instance, created, **kwargs):
    ''' Create affiliation if user is_owner == True (created via 'sign up'),
        if user is_owner == False (created via 'created Agent') do nothing
    '''

    if created:
        if instance.is_owner:
            Affiliation.objects.create(user=instance)
   

post_save.connect(post_user_created_singal, sender=User)