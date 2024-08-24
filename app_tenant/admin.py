from django.contrib import admin
from django.db import connection
from django.core.management import call_command
from .models import Client, Domain

class ClientAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change and obj.schema_name:
            if not self.schema_exists(obj.schema_name):
                try:
                    # Create schema and apply migrations for the new schema
                    call_command('migrate_schemas', schema_name=obj.schema_name, interactive=False)
                except Exception as e:
                    # Log or handle errors
                    print(f"Error during schema creation or migration: {e}")
                    raise

    def schema_exists(self, schema_name):
        """Check if the schema already exists in the database."""
        with connection.cursor() as cursor:
            cursor.execute("SELECT schema_name FROM information_schema.schemata WHERE schema_name = %s", [schema_name])
            return cursor.fetchone() is not None

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser and request.tenant.schema_name == 'public'

    def has_add_permission(self, request):
        return request.user.is_superuser and request.tenant.schema_name == 'public'

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser and request.tenant.schema_name == 'public'

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser and request.tenant.schema_name == 'public'


class DomainAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser and request.tenant.schema_name == 'public'

    def has_add_permission(self, request):
        return request.user.is_superuser and request.tenant.schema_name == 'public'

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser and request.tenant.schema_name == 'public'

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser and request.tenant.schema_name == 'public'


admin.site.register(Client, ClientAdmin)
admin.site.register(Domain, DomainAdmin)
