from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "yourairport_info.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import yourairport_info.users.signals  # noqa F401
        except ImportError:
            pass
