"""Test to ensure that the factories are working correctly."""

# AA EVE SDE Factory
from evesde_factory.eve_sde import (
    ConstellationFactory,
    ItemCategoryFactory,
    ItemGroupFactory,
    ItemTypeFactory,
    RegionFactory,
    SolarSystemFactory,
)
from evesde_factory.tests import EVESDEFactoryTestCase


class TestEveSdeFactory(EVESDEFactoryTestCase):
    """Test the factories."""

    def test_can_create_item_type(self):
        """Test that an item type can be created."""
        item_type = ItemTypeFactory()
        self.assertIsNotNone(item_type.id)

    def test_can_create_item_type_custom_name(self):
        """Test that an item type can be created with a custom name."""
        custom_name = "Custom Item Type"
        item_type = ItemTypeFactory(name=custom_name)
        self.assertIsNotNone(item_type.id)
        self.assertEqual(item_type.name, custom_name)

    def test_can_create_item_group(self):
        """Test that an item group can be created."""
        item_group = ItemGroupFactory()
        self.assertIsNotNone(item_group.id)

    def test_can_create_item_category(self):
        """Test that an item category can be created."""
        item_category = ItemCategoryFactory()
        self.assertIsNotNone(item_category.id)

    def test_can_create_region(self):
        """Test that a region can be created."""
        region = RegionFactory()
        self.assertIsNotNone(region.id)

    def test_can_create_constellation(self):
        """Test that a constellation can be created."""
        constellation = ConstellationFactory()
        self.assertIsNotNone(constellation.id)

    def test_can_create_solar_system(self):
        """Test that a solar system can be created."""
        solar_system = SolarSystemFactory()
        self.assertIsNotNone(solar_system.id)
