# from django.contrib.auth.mixins import AccessMixin
from django.http import HttpResponse

from .models import Lead


class OwnerRequiredMixin:
    """Verify that the current user is owner."""

    http_response_message = "You're not allowed to be here!"


    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_owner:
            return HttpResponse(self.http_response_message)
        return super().dispatch(request, *args, **kwargs)


class LeadsManagementAccessPermissionMixin:
    """Verify that the current user is owner."""

    http_response_message = "You're not allowed to be here!"


    def dispatch(self, request, *args, **kwargs):

        pk = kwargs['pk']

        if request.user.is_owner:
            lead = Lead.objects.get(id=pk)
            
            if lead.affiliation == request.user.affiliation:
                return super().dispatch(request, *args, **kwargs)
            else:
                return HttpResponse(self.http_response_message)
        
        elif request.user.is_agent:
            lead = Lead.objects.get(id=pk)
            
            if lead.affiliation == request.user.agent.affiliation:
                if lead.agent == None:
                    return HttpResponse(self.http_response_message)
                elif lead.agent == request.user.agent:
                    return super().dispatch(request, *args, **kwargs)
                else:
                    return HttpResponse(self.http_response_message)

        return HttpResponse(self.http_response_message) 