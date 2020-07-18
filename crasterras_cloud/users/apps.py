from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "crasterras_cloud.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import crasterras_cloud.users.signals  # noqa F401
        except ImportError:
            pass
