"""App URLs"""

# Django
from django.urls import path, re_path

# AA EVE SDE Factory
from evesde_factory import views
from evesde_factory.api import api

app_name: str = "evesde_factory"  # pylint: disable=invalid-name

urlpatterns = [
    path("", views.index, name="index"),
    # -- API System
    re_path(r"^api/", api.urls),
]
