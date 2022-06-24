from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    pass 


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
    age = models.IntegerField(default=0)

    source = models.CharField(max_length=100, choices=SOURCE_CHOICES)

    # on_delete=models.CASCADE
    # on_delete=models.SET_DEFAULT, default='name'
    agent = models.ForeignKey("Agent", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"({self.id})- {self.first_name} {self.last_name}"


class Agent(models.Model):

    user = models.OneToOneField("User", on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.id})- {self.user.email}"
