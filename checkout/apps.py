from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """ docstring """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        import checkout.signals
