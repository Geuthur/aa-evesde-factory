# Third Party
from ninja import NinjaAPI
from ninja.security import django_auth

# Django
from django.conf import settings

# AA EVE SDE Factory
from evesde_factory import __title__
from evesde_factory.api import character

api = NinjaAPI(
    title=f"{__title__} API",
    version="0.5.0",
    urls_namespace="evesde_factory:api",
    auth=django_auth,
    openapi_url=settings.DEBUG and "/openapi.json" or "",
)


def setup(ninja_api):
    character.CharacterApiEndpoints(ninja_api)


# Initialize API endpoints
setup(api)
