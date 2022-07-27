from django.contrib import admin

from .models import Lead, LeadStatus

# Register your models here.

admin.site.register(Lead)
admin.site.register(LeadStatus)


