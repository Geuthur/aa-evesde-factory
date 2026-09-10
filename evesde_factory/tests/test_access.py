"""Template for a TestView class."""

# Standard Library
from http import HTTPStatus

# Django
from django.urls import reverse

# AA EVE SDE Factory
from evesde_factory import views
from evesde_factory.tests import EVESDEFactoryTestCase


class TestViews(EVESDEFactoryTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    # def test_index(self):
    #    """
    #    Test should render index view.
    #    """
    #    # given
    #    request = self.factory.get(reverse("evesde_factory:index"))
    #    request.user = self.user
    #    # when
    #    response = views.index(request)
    #    # then
    #    self.assertEqual(response.status_code, HTTPStatus.OK)
    #    self.assertContains(response, "Example")
