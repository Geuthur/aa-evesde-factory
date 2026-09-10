"""Template for a TestView class."""

# Standard Library
from http import HTTPStatus

# Django
from django.urls import reverse

# AA EVE SDE Factory
from evesde_factory import __title__, views
from evesde_factory.tests import ExampleTestCase


class TestViews(ExampleTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_index(self):
        """
        Test should render index view.
        """
        # given
        request = self.factory.get(reverse("evesde_factory:index"))
        request.user = self.user
        # when
        response = views.index(request)
        # then
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, __title__)

    def test_index_denies_user_without_permission(self):
        """
        Test should deny access to user without the app permission.
        """
        # given
        self.user.user_permissions.clear()
        self.user.refresh_from_db()
        for attr in ("_perm_cache", "_user_perm_cache", "_group_perm_cache"):
            if hasattr(self.user, attr):
                delattr(self.user, attr)
        request = self.factory.get(reverse("evesde_factory:index"))
        request.user = self.user
        # when
        response = views.index(request)
        # then
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertIn("next=", response.url)
