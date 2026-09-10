"""PvE Views"""

# Django
from django.contrib.auth.decorators import login_required, permission_required
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

# Alliance Auth
from allianceauth.services.hooks import get_extension_logger

# AA EVE SDE Factory
from evesde_factory import __title__
from evesde_factory.providers import AppLogger

logger = AppLogger(get_extension_logger(__name__), __title__)


@login_required
@permission_required("evesde_factory.basic_access")
def index(request: WSGIRequest):
    """Index View"""
    context = {
        "title": __title__,
    }
    return render(request, "evesde_factory/view-index.html", context=context)
