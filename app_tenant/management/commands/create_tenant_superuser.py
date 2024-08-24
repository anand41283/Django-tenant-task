# app_tenant/management/commands/create_tenant_superuser.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django_tenants.utils import tenant_context
from app_tenant.models import Client  # Adjust import if necessary


class Command(BaseCommand):
    help = 'Create a superuser for a specific tenant schema'

    def add_arguments(self, parser):
        parser.add_argument('tenant_name', type=str, help='Name of the tenant schema')
        parser.add_argument('--username', type=str, default='admin', help='Username for the superuser')
        parser.add_argument('--email', type=str, default='admin@example.com', help='Email for the superuser')
        parser.add_argument('--password', type=str, default='password123', help='Password for the superuser')

    def handle(self, *args, **kwargs):
        tenant_name = kwargs['tenant_name']
        username = kwargs['username']
        email = kwargs['email']
        password = kwargs['password']

        try:
            tenant = Client.objects.get(name=tenant_name)
        except Client.DoesNotExist:
            self.stderr.write(self.style.ERROR(f'Tenant with name "{tenant_name}" does not exist.'))
            return

        with tenant_context(tenant):
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS(f'Superuser created for tenant "{tenant_name}".'))
