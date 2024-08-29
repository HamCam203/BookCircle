from django.apps import AppConfig


class BookcConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookc'

    def ready(self):
        from bookc import signals
