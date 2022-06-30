from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


# Create your models here.

class User(AbstractUser):
    pass 


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
    age = models.IntegerField(default=0)

    source = models.CharField(max_length=100, choices=SOURCE_CHOICES)

    # on_delete=models.CASCADE
    # on_delete=models.SET_DEFAULT, default='name'
    agent = models.ForeignKey("Agent", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Agent(models.Model):

    user = models.OneToOneField("User", on_delete=models.CASCADE)
    affiliation = models.ForeignKey("Affiliation", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.email}"


# Signals 

def post_user_created_singal(sender, instance, created, **kwargs):
    
    # print(instance, created, sender)
    if created:
        Affiliation.objects.create(user=instance)
    else:
        pass
    

post_save.connect(post_user_created_singal, sender=User)