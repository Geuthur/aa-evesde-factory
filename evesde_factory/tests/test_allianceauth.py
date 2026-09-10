"""Test to ensure that the factories are working correctly."""

# Alliance Auth
from allianceauth.authentication.models import Permission, User

# AA EVE SDE Factory
from evesde_factory.allianceauth import (
    EveAllianceInfoFactory,
    EveCharacterFactory,
    EveCorporationInfoFactory,
    UserFactory,
    UserMainFactory,
)
from evesde_factory.tests import EVESDEFactoryTestCase


class TestAllianceAuthFactory(EVESDEFactoryTestCase):
    """Test the factories."""

    def test_can_create_user(self):
        """Test that a user can be created."""
        user = UserFactory()
        self.assertTrue(user)
        self.assertIsNotNone(User.objects.get(id=user.id))

    def test_can_create_app_user(self):
        """Test that an app user can be created."""
        user = UserMainFactory()
        self.assertTrue(user.has_perm("corputils.view_corp_corpstats"))

    def test_can_create_app_user_with_custom_permissions(self):
        """Test that an app user can be created with custom permissions."""
        user = UserMainFactory(permissions__=["corputils.view_state_corpstats"])
        self.assertTrue(user.has_perm("corputils.view_state_corpstats"))

    def test_can_create_eve_character(self):
        """Test that an EVE character can be created."""
        character = EveCharacterFactory()
        self.assertIsNotNone(character.character_id)

    def test_can_create_eve_corporation(self):
        """Test that an EVE corporation can be created."""
        corporation = EveCorporationInfoFactory()
        self.assertIsNotNone(corporation.corporation_id)

    def test_can_create_eve_alliance(self):
        """Test that an EVE alliance can be created."""
        alliance = EveAllianceInfoFactory()
        self.assertIsNotNone(alliance.alliance_id)
