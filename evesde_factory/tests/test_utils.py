"""Tests for the helper functions."""

# AA EVE SDE Factory
from evesde_factory.allianceauth import UserFactory
from evesde_factory.tests import AuthTestCase
from evesde_factory.utils import add_permission_to_user


class TestAddPermissionToUser(AuthTestCase):
    """Test add_permission_to_user."""

    def test_should_add_all_permissions(self):
        """Test that every permission of the list is granted, not only the first."""
        user = UserFactory()
        permissions = [
            "corputils.view_corp_corpstats",
            "corputils.view_alliance_corpstats",
            "corputils.view_state_corpstats",
        ]

        result = add_permission_to_user(user, permissions)

        for permission in permissions:
            self.assertTrue(result.has_perm(permission))

    def test_should_raise_error_when_no_permissions(self):
        """Test that an empty list raises a ValueError."""
        user = UserFactory()

        with self.assertRaises(ValueError):
            add_permission_to_user(user, [])
