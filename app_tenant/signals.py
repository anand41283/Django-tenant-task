# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django_tenants.utils import schema_context
# from django.core.management import call_command
# from .models import Client
#
# @receiver(post_save, sender=Client)
# def run_migrations_on_new_tenant(sender, instance, created, **kwargs):
#     if created:
#         with schema_context(instance.schema_name):
#             # Ensure schema is created before applying migrations
#             call_command('migrate_schemas', schema_name=instance.schema_name)
