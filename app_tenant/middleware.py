import logging
from django.http import HttpResponseForbidden
from django_tenants.utils import get_tenant_model
from django.utils.deprecation import MiddlewareMixin
from django.core.exceptions import PermissionDenied

logger = logging.getLogger(__name__)

class TenantPermissionMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if not request.user.is_authenticated:
            return None

        tenant_model = get_tenant_model()
        try:
            tenant = tenant_model.objects.get(schema_name=request.tenant.schema_name)
        except tenant_model.DoesNotExist:
            return HttpResponseForbidden("Tenant does not exist.")

        user = request.user

        logger.debug(f"User: {user.username}, Tenant: {tenant.name}, Schema: {tenant.schema_name}")

        # Allow superusers full access in the public schema
        if user.is_superuser and request.tenant.schema_name == 'public':
            return None

        # Check if the user is accessing the admin panel
        if request.path.startswith('/admin/'):
            if not user.is_staff:
                raise PermissionDenied("You don't have permission to access the admin panel.")

        return None
