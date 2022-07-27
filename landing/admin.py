from django.contrib import admin

from .models import User, Affiliation

# Register your models here.

admin.site.register(User)
admin.site.register(Affiliation)
