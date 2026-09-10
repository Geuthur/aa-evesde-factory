"""App Configuration"""

# Django
from django.apps import AppConfig

# AA EVE SDE Factory
from evesde_factory import __title__, __version__


class EvesdeFactoryConfig(AppConfig):
    """App Config"""

    default_auto_field = "django.db.models.AutoField"
    name = "evesde_factory"
    label = "evesde_factory"
    verbose_name = f"{__title__} v{__version__}"
