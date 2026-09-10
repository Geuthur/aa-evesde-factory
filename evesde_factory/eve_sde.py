# Third Party
import factory
import factory.fuzzy

# Alliance Auth (External Libs)
from eve_sde.models import (
    Constellation,
    ItemCategory,
    ItemGroup,
    ItemType,
    Planet,
    Region,
    SolarSystem,
)

# AA EVE SDE Factory
# pylint: disable=unused-import
from evesde_factory.allianceauth import BaseMetaFactory


class ItemCategoryFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[ItemCategory]
):
    """Generate an ItemCategory object for testing."""

    class Meta:
        model = ItemCategory
        django_get_or_create = ("id",)

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker("word")
    published = True
    icon_id = factory.fuzzy.FuzzyInteger(0, 100)


class ItemGroupFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[ItemGroup]
):
    """Generate an ItemGroup object for testing."""

    class Meta:
        model = ItemGroup
        django_get_or_create = ("id",)

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker("word")
    anchorable = False
    anchored = False
    category = factory.SubFactory(ItemCategoryFactory)
    fittable_non_singleton = False
    icon_id = factory.fuzzy.FuzzyInteger(0, 100)
    published = True
    use_base_price = False


class ItemTypeFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[ItemType]
):
    """Generate an ItemType object for testing."""

    class Meta:
        model = ItemType
        django_get_or_create = ("id",)

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker("word")
    base_price = factory.fuzzy.FuzzyFloat(1, 10000, 2)
    capacity = factory.fuzzy.FuzzyFloat(0, 1000, 2)
    description = factory.Faker("sentence")
    faction_id_raw = factory.fuzzy.FuzzyInteger(0, 100)
    graphic_id = factory.fuzzy.FuzzyInteger(0, 100)
    group = factory.SubFactory(ItemGroupFactory)
    icon_id = factory.fuzzy.FuzzyInteger(0, 100)
    market_group = None  # This can be set to a MarketGroup object if needed
    mass = factory.fuzzy.FuzzyDecimal(0, 1000, 2)
    meta_group_id_raw = factory.fuzzy.FuzzyInteger(0, 10)
    portion_size = factory.fuzzy.FuzzyInteger(0, 1000)
    published = True
    race_id = factory.fuzzy.FuzzyInteger(0, 10)
    radius = factory.fuzzy.FuzzyFloat(0, 1000, 2)
    sound_id = None  # Not needed for testing, can be set to a Sound object if needed
    variation_parent_type_id = (
        None  # Not needed for testing, can be set to an ItemType object if needed
    )
    volume = factory.fuzzy.FuzzyFloat(0, 1000, 2)
    packaged_volume = factory.fuzzy.FuzzyFloat(0, 1000, 2)


class RegionFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[Region]
):
    """Generate a Region object for testing."""

    class Meta:
        model = Region
        django_get_or_create = ("id",)

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker("word")
    x = factory.fuzzy.FuzzyFloat(-1000, 1000, 2)
    y = factory.fuzzy.FuzzyFloat(-1000, 1000, 2)
    z = factory.fuzzy.FuzzyFloat(-1000, 1000, 2)

    description = factory.Faker("sentence")
    faction_id_raw = factory.fuzzy.FuzzyInteger(0, 100)
    nebular_id_raw = factory.fuzzy.FuzzyInteger(0, 100)
    wormhole_class_id_raw = factory.fuzzy.FuzzyInteger(0, 10)


class ConstellationFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[Constellation]
):
    """Generate a Constellation object for testing."""

    class Meta:
        model = Constellation
        django_get_or_create = ("id",)

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker("word")
    x = factory.fuzzy.FuzzyFloat(-1000, 1000, 2)
    y = factory.fuzzy.FuzzyFloat(-1000, 1000, 2)
    z = factory.fuzzy.FuzzyFloat(-1000, 1000, 2)

    region = factory.SubFactory(RegionFactory)
    faction_id_raw = factory.fuzzy.FuzzyInteger(0, 100)
    wormhole_class_id_raw = factory.fuzzy.FuzzyInteger(0, 10)


class SolarSystemFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[SolarSystem]
):
    """Generate a SolarSystem object for testing."""

    class Meta:
        model = SolarSystem
        django_get_or_create = ("id",)

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker("word")
    x = factory.fuzzy.FuzzyFloat(-1000, 1000, 2)
    y = factory.fuzzy.FuzzyFloat(-1000, 1000, 2)
    z = factory.fuzzy.FuzzyFloat(-1000, 1000, 2)

    border = False
    constellation = factory.SubFactory(ConstellationFactory)
    corridor = False
    faction_id_raw = factory.fuzzy.FuzzyInteger(0, 100)
    fringe = False
    hub = False
    international = False
    luminosity = factory.fuzzy.FuzzyFloat(0, 1000, 2)
    radius = factory.fuzzy.FuzzyFloat(0, 1000, 2)
    regional = False
    security_class = factory.fuzzy.FuzzyChoice([None, "A", "B", "C", "D", "E"])
    security_status = factory.fuzzy.FuzzyFloat(0, 1, 2)
    visual_effect = (
        None  # Not needed for testing, can be set to a VisualEffect object if needed
    )
    wormhole_class_id_raw = factory.fuzzy.FuzzyInteger(0, 10)
    security_status = factory.fuzzy.FuzzyFloat(0, 1, 2)

    x_2d = factory.fuzzy.FuzzyFloat(-1000, 1000, 2)
    y_2d = factory.fuzzy.FuzzyFloat(-1000, 1000, 2)


class PlanetFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[Planet]
):
    """Generate a Planet object for testing."""

    class Meta:
        model = Planet
        django_get_or_create = ("id",)

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker("word")

    x = factory.fuzzy.FuzzyFloat(-1000, 1000, 2)
    y = factory.fuzzy.FuzzyFloat(-1000, 1000, 2)
    z = factory.fuzzy.FuzzyFloat(-1000, 1000, 2)

    celestial_index = factory.fuzzy.FuzzyInteger(1, 100)
    item_type = factory.SubFactory(ItemTypeFactory)
    orbit_id_raw = factory.fuzzy.FuzzyInteger(1, 100)
    orbit_index = factory.fuzzy.FuzzyInteger(1, 100)
    radius = factory.fuzzy.FuzzyFloat(1, 1000, 2)
    solar_system = factory.SubFactory(SolarSystemFactory)
