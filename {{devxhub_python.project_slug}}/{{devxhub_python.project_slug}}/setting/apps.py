from django.apps import AppConfig


class SettingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '{{ devxhub_python.project_slug }}.setting'
