# from django.contrib.auth.mixins import AccessMixin
from django.http import HttpResponse, Http404

from .models import Lead


class OwnerRequiredMixin:
    """Verify that the current user is owner."""

    http_response_message = "You're not allowed to be here!"


    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_owner:
            return HttpResponse(self.http_response_message)
        return super().dispatch(request, *args, **kwargs)


class LeadsManagementAccessPermissionMixin:
    """Verify that the current user has access to a lead"""

    http_response_message = "You're not allowed to be here!"
    # lead = None

    # def dispatch(self, request, *args, **kwargs):

    #     if request.user.is_owner:
    #         self.get_object()
            
    #         if self.lead.affiliation == request.user.affiliation:
    #             return super().dispatch(request, *args, **kwargs)
    #         else:
    #             return HttpResponse(self.http_response_message)
        
    #     elif request.user.is_agent:
    #         self.get_object()
            
    #         if self.lead.affiliation == request.user.agent.affiliation:
    #             if self.lead.agent == None:
    #                 return HttpResponse(self.http_response_message)
    #             elif self.lead.agent == request.user.agent:
    #                 return super().dispatch(request, *args, **kwargs)
    #             else:
    #                 return HttpResponse(self.http_response_message)

    #     return HttpResponse(self.http_response_message)

    
    # def get_object(self):
        
    #     if self.lead is not None:
    #         return self.lead
        
    #     if self.queryset is None:
    #         queryset = self.get_queryset()
        
    #     pk = self.kwargs.get(self.pk_url_kwarg)
    #     if pk is not None:
    #         queryset = queryset.filter(pk=pk)
    #     else:
    #         raise AttributeError(
    #         "Generic detail view %s must be called with either an object "
    #         "pk in the URLconf." % self.__class__.__name__
    #         )
        
    #     try:
    #         # Get the single item from the filtered queryset
    #         self.lead = queryset.get()
    #     except queryset.model.DoesNotExist:
    #         raise Http404("Not found")
        
    #     return self.lead

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        lead = self.object
        context = self.get_context_data(object=self.object)

        if request.user.is_owner:
            if lead.affiliation == request.user.affiliation:
                return self.render_to_response(context)
            else:
                return HttpResponse(self.http_response_message)
        
        elif request.user.is_agent:
            if lead.agent == request.user.agent:
                    return self.render_to_response(context)
            else:
                return HttpResponse(self.http_response_message)

        return HttpResponse(self.http_response_message)



