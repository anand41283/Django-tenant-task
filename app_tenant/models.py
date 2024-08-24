from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django.core.management import call_command


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
    subscription_plan = models.CharField(
        max_length=20,
        choices=[
            ('basic', 'Basic'),
            ('premium', 'Premium'),
            ('professional', 'Professional')
        ],
        default='basic'
    )

    def save(self, *args, **kwargs):
        # Ensure schema_name is set and valid
        if not self.schema_name:
            raise ValueError("schema_name must be set for a Client")

        super().save(*args, **kwargs)

        # Create schema and apply migrations
        call_command('migrate_schemas', schema_name=self.schema_name, interactive=False)


class Domain(DomainMixin):
    pass

