from django.apps import AppConfig


class AppTenantsConfig(AppConfig):
    name = 'app_tenant'

    def ready(self):
        import app_tenant.signals   # Import the signals module
