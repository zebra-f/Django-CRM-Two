from django.contrib.auth.mixins import AccessMixin
from django.http import HttpResponse


class OwnerRequiredMixin(AccessMixin):
    """Verify that the current user is owner."""

    http_reponse_message = "You're not allowed to be here!"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_owner:
            return HttpResponse(self.http_reponse_message)
        return super().dispatch(request, *args, **kwargs)