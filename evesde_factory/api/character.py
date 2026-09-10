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
    tags = ["Example"]

    def __init__(self, api: NinjaAPI):
        @api.get(
            "evesde_factory/",
            response={
                HTTPStatus.OK: list[schema.ExampleSchema],
                HTTPStatus.FORBIDDEN: dict,
            },
            tags=self.tags,
        )
        def get_example(request):
            """
            Get Example Data

            This endpoint retrieves evesde_factory data for the authenticated user.

            Returns:
                200: Example data retrieved successfully.
                403: Permission Denied.
            """
            user = request.user
            if not user.is_superuser:
                return HTTPStatus.FORBIDDEN, {"error": _("Permission Denied.")}

            # Example data - replace this with your actual logic
            example_data = [
                schema.ExampleSchema(
                    id=1,
                    name="Example 1",
                    description="This is an evesde_factory.",
                ),
                schema.ExampleSchema(
                    id=2,
                    name="Example 2",
                    description="This is another evesde_factory.",
                ),
            ]

            return HTTPStatus.OK, example_data
