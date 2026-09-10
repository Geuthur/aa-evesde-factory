"""PvE Views"""

# Django
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

# AA EVE SDE Factory
from evesde_factory import __title__


@login_required
def index(request: WSGIRequest):
    """Index View"""
    context = {
        "title": "Example",
    }
    return render(request, "evesde_factory/view-index.html", context=context)
