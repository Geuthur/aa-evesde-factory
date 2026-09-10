# Third Party

# Standard Library
from http import HTTPStatus

# Third Party
from ninja import NinjaAPI

# Django
from django.utils.translation import gettext_lazy as _

# Alliance Auth
from allianceauth.services.hooks import get_extension_logger

# AA EVE SDE Factory
from evesde_factory import __title__
from evesde_factory.api import schema
from evesde_factory.providers import AppLogger

logger = AppLogger(get_extension_logger(__name__), __title__)


class CharacterApiEndpoints:
    tags = [__title__]

    def __init__(self, api: NinjaAPI):
        @api.get(
            "evesde_factory/",
            response={
                HTTPStatus.OK: list[schema.ExampleSchema],
                HTTPStatus.FORBIDDEN: dict,
            },
            tags=self.tags,
        )
        def get_evesde_factory(request):
            """
            Get AA EVE SDE Factory Data

            This endpoint retrieves evesde_factory data for the authenticated user.

            Returns:
                200: AA EVE SDE Factory data retrieved successfully.
                403: Permission Denied.
            """
            user = request.user
            if not user.is_superuser:
                return HTTPStatus.FORBIDDEN, {"error": _("Permission Denied.")}

            # AA EVE SDE Factory data - replace this with your actual logic
            example_data = [
                schema.ExampleSchema(
                    character_id=1,
                    character_name="AA EVE SDE Factory Character 1",
                    corporation_id=1001,
                    corporation_name="AA EVE SDE Factory Corporation 1",
                ),
                schema.ExampleSchema(
                    character_id=2,
                    character_name="AA EVE SDE Factory Character 2",
                    corporation_id=1002,
                    corporation_name="AA EVE SDE Factory Corporation 2",
                ),
            ]

            return HTTPStatus.OK, example_data
