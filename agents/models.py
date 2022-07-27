from django.db import models

from landing.models import User, Affiliation 

# Create your models here.

class Agent(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    affiliation = models.ForeignKey(Affiliation, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"