from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

# Create your models here.

class User(AbstractUser):
    is_owner = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class Affiliation(models.Model):
    name = models.CharField(max_length=200, null=True)
    owner = models.OneToOneField("User", on_delete=models.CASCADE)

    def __str__(self):
        if self.name:
            return f"{self.owner.username}, {self.name}"
        else:
            return self.owner.username

# Signals 

def post_user_created_singal(sender, instance, created, **kwargs):
    ''' Create affiliation if user is_owner == True (created via 'sign up'),
        if user is_owner == False (created via 'created Agent') do nothing
    '''

    if created:
        if instance.is_owner:
            Affiliation.objects.create(owner=instance)
   

post_save.connect(post_user_created_singal, sender=User)
