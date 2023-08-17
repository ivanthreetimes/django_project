from django.apps import AppConfig


class AppUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_project.app_users'

    def ready(self):
        import django_project.app_users.signals
