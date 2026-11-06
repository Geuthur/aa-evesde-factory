# Third Party
import factory
import factory.fuzzy

# Alliance Auth (External Libs)
from eve_sde.models import (
    AccountingEntryType,
    Archetype,
    BlueprintActivity,
    BlueprintActivityMaterial,
    BlueprintActivityProduct,
    Certificate,
    CertificateRecommendedType,
    CertificateSkill,
    Constellation,
    CorporationRole,
    CorporationRoleGroup,
    CorporationRoleGroupMembership,
    DogmaAttribute,
    DogmaAttributeCategory,
    DogmaEffect,
    DogmaUnit,
    FreelanceJobSchema,
    FreelanceJobSchemaParameter,
    ItemCategory,
    ItemGroup,
    ItemMarketGroup,
    ItemType,
    ItemTypeMaterials,
    Landmark,
    Mastery,
    MetenoxMoonDrill,
    Moon,
    NotificationType,
    NPCStation,
    Planet,
    PlanetResource,
    Region,
    SkillPlan,
    SkillPlanMilestone,
    SkillPlanSkillRequirement,
    SolarSystem,
    SovereigntyUpgrade,
    Star,
    Stargate,
    StarResource,
    TypeDogma,
    TypeEffect,
    TypeList,
    TypeListCategory,
    TypeListGroup,
    TypeListType,
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
    mass = factory.fuzzy.FuzzyFloat(0, 1000, 2)
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
    radius = factory.fuzzy.FuzzyInteger(1, 100000)
    solar_system = factory.SubFactory(SolarSystemFactory)


class ItemMarketGroupFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[ItemMarketGroup]
):
    """Generate an ItemMarketGroup object for testing."""

    class Meta:
        model = ItemMarketGroup
        django_get_or_create = ("id",)

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker("word")
    description = factory.Faker("sentence")
    has_types = True
    icon_id = factory.fuzzy.FuzzyInteger(0, 100)
    parent_group = None  # This can be set to an ItemMarketGroup object if needed


class ItemTypeMaterialsFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[ItemTypeMaterials]
):
    """Generate an ItemTypeMaterials object for testing."""

    class Meta:
        model = ItemTypeMaterials

    item_type = factory.SubFactory(ItemTypeFactory)
    material_item_type = factory.SubFactory(ItemTypeFactory)
    quantity = factory.fuzzy.FuzzyInteger(1, 1000)


class TypeListFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[TypeList]
):
    """Generate a TypeList object for testing."""

    class Meta:
        model = TypeList
        django_get_or_create = ("id",)

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker("word")
    internal_name = factory.Faker("word")
    description = factory.Faker("sentence")


class TypeListTypeFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[TypeListType]
):
    """Generate a TypeListType object for testing."""

    class Meta:
        model = TypeListType

    type_list = factory.SubFactory(TypeListFactory)
    item_type = factory.SubFactory(ItemTypeFactory)
    excluded = False


class TypeListGroupFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[TypeListGroup]
):
    """Generate a TypeListGroup object for testing."""

    class Meta:
        model = TypeListGroup

    type_list = factory.SubFactory(TypeListFactory)
    item_group = factory.SubFactory(ItemGroupFactory)
    excluded = False


class TypeListCategoryFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[TypeListCategory]
):
    """Generate a TypeListCategory object for testing."""

    class Meta:
        model = TypeListCategory

    type_list = factory.SubFactory(TypeListFactory)
    item_category = factory.SubFactory(ItemCategoryFactory)
    excluded = False


class DogmaAttributeCategoryFactory(
    factory.django.DjangoModelFactory,
    metaclass=BaseMetaFactory[DogmaAttributeCategory],
):
    """Generate a DogmaAttributeCategory object for testing."""

    class Meta:
        model = DogmaAttributeCategory
        django_get_or_create = ("id",)

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker("word")
    description = factory.Faker("sentence")


class DogmaUnitFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[DogmaUnit]
):
    """Generate a DogmaUnit object for testing."""

    class Meta:
        model = DogmaUnit
        django_get_or_create = ("id",)

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker("word")
    description = factory.Faker("sentence")
    display_name = factory.Faker("word")


class DogmaAttributeFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[DogmaAttribute]
):
    """Generate a DogmaAttribute object for testing."""

    class Meta:
        model = DogmaAttribute
        django_get_or_create = ("id",)

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker("word")
    attribute_category = factory.SubFactory(DogmaAttributeCategoryFactory)
    default_value = factory.fuzzy.FuzzyFloat(0, 1000, 2)
    description = factory.Faker("sentence")
    display_name = factory.Faker("word")
    high_is_good = True
    icon_id = factory.fuzzy.FuzzyInteger(0, 100)
    published = True
    stackable = True
    unit = factory.SubFactory(DogmaUnitFactory)


class DogmaEffectFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[DogmaEffect]
):
    """Generate a DogmaEffect object for testing."""

    class Meta:
        model = DogmaEffect
        django_get_or_create = ("id",)

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker("word")
    description = factory.Faker("sentence")
    display_name = factory.Faker("word")
    effect_category_id_raw = factory.fuzzy.FuzzyInteger(0, 10)
    icon_id = factory.fuzzy.FuzzyInteger(0, 100)
    published = True


class TypeEffectFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[TypeEffect]
):
    """Generate a TypeEffect object for testing."""

    class Meta:
        model = TypeEffect

    item_type = factory.SubFactory(ItemTypeFactory)
    dogma_effect = factory.SubFactory(DogmaEffectFactory)
    is_default = False


class TypeDogmaFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[TypeDogma]
):
    """Generate a TypeDogma object for testing."""

    class Meta:
        model = TypeDogma

    item_type = factory.SubFactory(ItemTypeFactory)
    dogma_attribute = factory.SubFactory(DogmaAttributeFactory)
    value = factory.fuzzy.FuzzyFloat(0, 1000, 2)


class CertificateFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[Certificate]
):
    """Generate a Certificate object for testing."""

    class Meta:
        model = Certificate
        django_get_or_create = ("id",)

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker("word")
    description = factory.Faker("sentence")
    group = factory.SubFactory(ItemGroupFactory)


class CertificateSkillFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[CertificateSkill]
):
    """Generate a CertificateSkill object for testing."""

    class Meta:
        model = CertificateSkill

    certificate = factory.SubFactory(CertificateFactory)
    item_type = factory.SubFactory(ItemTypeFactory)
    basic = 1
    standard = 2
    improved = 3
    advanced = 4
    elite = 5


class CertificateRecommendedTypeFactory(
    factory.django.DjangoModelFactory,
    metaclass=BaseMetaFactory[CertificateRecommendedType],
):
    """Generate a CertificateRecommendedType object for testing."""

    class Meta:
        model = CertificateRecommendedType

    certificate = factory.SubFactory(CertificateFactory)
    item_type = factory.SubFactory(ItemTypeFactory)


class MasteryFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[Mastery]
):
    """Generate a Mastery object for testing."""

    class Meta:
        model = Mastery

    item_type = factory.SubFactory(ItemTypeFactory)
    level = factory.Sequence(lambda n: n % 5)
    certificate = factory.SubFactory(CertificateFactory)


class ArchetypeFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[Archetype]
):
    """Generate an Archetype object for testing."""

    class Meta:
        model = Archetype
        django_get_or_create = ("id",)

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker("word")
    description = factory.Faker("sentence")


class StarFactory(factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[Star]):
    """Generate a Star object for testing."""

    class Meta:
        model = Star
        django_get_or_create = ("id",)

    id = factory.Sequence(lambda n: n + 1)
    x = factory.fuzzy.FuzzyFloat(-1000, 1000, 2)
    y = factory.fuzzy.FuzzyFloat(-1000, 1000, 2)
    z = factory.fuzzy.FuzzyFloat(-1000, 1000, 2)

    age = factory.fuzzy.FuzzyFloat(0, 1000, 2)
    item_type = factory.SubFactory(ItemTypeFactory)
    life = factory.fuzzy.FuzzyFloat(0, 1000, 2)
    luminosity = factory.fuzzy.FuzzyFloat(0, 1000, 2)
    radius = factory.fuzzy.FuzzyInteger(1, 100000)
    solar_system = factory.SubFactory(SolarSystemFactory)
    spectral_class = factory.fuzzy.FuzzyChoice(["G5 V", "K2 V", "M0 V"])
    temperature = factory.fuzzy.FuzzyFloat(1000, 10000, 2)


class StargateFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[Stargate]
):
    """Generate a Stargate object for testing."""

    class Meta:
        model = Stargate
        django_get_or_create = ("id",)

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker("word")
    x = factory.fuzzy.FuzzyFloat(-1000, 1000, 2)
    y = factory.fuzzy.FuzzyFloat(-1000, 1000, 2)
    z = factory.fuzzy.FuzzyFloat(-1000, 1000, 2)

    destination = factory.SubFactory(SolarSystemFactory)
    item_type = factory.SubFactory(ItemTypeFactory)
    solar_system = factory.SubFactory(SolarSystemFactory)


class NPCStationFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[NPCStation]
):
    """Generate an NPCStation object for testing."""

    class Meta:
        model = NPCStation
        django_get_or_create = ("id",)

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker("word")
    x = factory.fuzzy.FuzzyFloat(-1000, 1000, 2)
    y = factory.fuzzy.FuzzyFloat(-1000, 1000, 2)
    z = factory.fuzzy.FuzzyFloat(-1000, 1000, 2)

    celestial_index = factory.fuzzy.FuzzyInteger(1, 100)
    operation_id_raw = factory.fuzzy.FuzzyInteger(1, 100)
    orbit_id_raw = factory.fuzzy.FuzzyInteger(1, 100)
    orbit_index = factory.fuzzy.FuzzyInteger(1, 100)
    owner_id_raw = factory.fuzzy.FuzzyInteger(1000000, 1000999)
    reprocessing_efficiency = 0.5
    reprocessing_hangar_flag = 4
    reprocessing_stations_take = 0.05
    solar_system = factory.SubFactory(SolarSystemFactory)
    item_type = factory.SubFactory(ItemTypeFactory)
    use_operation_name = True


class PlanetResourceFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[PlanetResource]
):
    """Generate a PlanetResource object for testing."""

    class Meta:
        model = PlanetResource
        django_get_or_create = ("planet",)

    planet = factory.SubFactory(PlanetFactory)
    power = factory.fuzzy.FuzzyInteger(0, 1000)
    workforce = factory.fuzzy.FuzzyInteger(0, 1000)


class StarResourceFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[StarResource]
):
    """Generate a StarResource object for testing."""

    class Meta:
        model = StarResource
        django_get_or_create = ("star",)

    star = factory.SubFactory(StarFactory)
    power = factory.fuzzy.FuzzyInteger(0, 1000)
    workforce = factory.fuzzy.FuzzyInteger(0, 1000)


class MoonFactory(factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[Moon]):
    """Generate a Moon object for testing."""

    class Meta:
        model = Moon
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
    planet = factory.SubFactory(PlanetFactory)
    radius = factory.fuzzy.FuzzyInteger(1, 100000)
    solar_system = factory.LazyAttribute(
        lambda o: o.planet.solar_system if o.planet else None
    )


class LandmarkFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[Landmark]
):
    """Generate a Landmark object for testing."""

    class Meta:
        model = Landmark
        django_get_or_create = ("id",)

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker("word")
    x = factory.fuzzy.FuzzyFloat(-1000, 1000, 2)
    y = factory.fuzzy.FuzzyFloat(-1000, 1000, 2)
    z = factory.fuzzy.FuzzyFloat(-1000, 1000, 2)

    description = factory.Faker("sentence")
    icon_id = factory.fuzzy.FuzzyInteger(0, 100)
    solar_system = factory.SubFactory(SolarSystemFactory)


class FreelanceJobSchemaFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[FreelanceJobSchema]
):
    """Generate a FreelanceJobSchema object for testing."""

    class Meta:
        model = FreelanceJobSchema
        django_get_or_create = ("id",)

    id = factory.Sequence(lambda n: f"schema-{n + 1}")
    title = factory.Faker("sentence", nb_words=3)
    description = factory.Faker("sentence")


class FreelanceJobSchemaParameterFactory(
    factory.django.DjangoModelFactory,
    metaclass=BaseMetaFactory[FreelanceJobSchemaParameter],
):
    """Generate a FreelanceJobSchemaParameter object for testing."""

    class Meta:
        model = FreelanceJobSchemaParameter
        django_get_or_create = ("id",)

    schema = factory.SubFactory(FreelanceJobSchemaFactory)
    key = factory.Sequence(lambda n: f"param_{n + 1}")
    id = factory.LazyAttribute(lambda o: f"{o.schema.id}:{o.key}")
    kind = "matcher"
    title = factory.Faker("word")
    description = factory.Faker("sentence")


class BlueprintActivityFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[BlueprintActivity]
):
    """Generate a BlueprintActivity object for testing."""

    class Meta:
        model = BlueprintActivity
        django_get_or_create = ("id",)

    blueprint_item_type = factory.SubFactory(ItemTypeFactory)
    activity = BlueprintActivity.Activities.manufacturing
    id = factory.LazyAttribute(
        lambda o: BlueprintActivity.build_pk(o.blueprint_item_type.id, o.activity)
    )
    time = factory.fuzzy.FuzzyInteger(60, 86400)
    max_production_limit = factory.fuzzy.FuzzyInteger(1, 1000)


class BlueprintActivityProductFactory(
    factory.django.DjangoModelFactory,
    metaclass=BaseMetaFactory[BlueprintActivityProduct],
):
    """Generate a BlueprintActivityProduct object for testing."""

    class Meta:
        model = BlueprintActivityProduct

    blueprint_activity = factory.SubFactory(BlueprintActivityFactory)
    item_type = factory.SubFactory(ItemTypeFactory)
    quantity = factory.fuzzy.FuzzyInteger(1, 100)
    probability = None  # Only used for invention activities


class BlueprintActivityMaterialFactory(
    factory.django.DjangoModelFactory,
    metaclass=BaseMetaFactory[BlueprintActivityMaterial],
):
    """Generate a BlueprintActivityMaterial object for testing."""

    class Meta:
        model = BlueprintActivityMaterial

    blueprint_activity = factory.SubFactory(BlueprintActivityFactory)
    item_type = factory.SubFactory(ItemTypeFactory)
    quantity = factory.fuzzy.FuzzyInteger(1, 1000)


class AccountingEntryTypeFactory(
    factory.django.DjangoModelFactory,
    metaclass=BaseMetaFactory[AccountingEntryType],
):
    """Generate an AccountingEntryType object for testing."""

    class Meta:
        model = AccountingEntryType
        django_get_or_create = ("id",)

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker("word")
    internal_name = factory.Faker("word")
    description = factory.Faker("sentence")
    journal_message = factory.Faker("sentence")


class NotificationTypeFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[NotificationType]
):
    """Generate a NotificationType object for testing."""

    class Meta:
        model = NotificationType
        django_get_or_create = ("id",)

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker("word")
    internal_name = factory.Faker("word")


class CorporationRoleGroupFactory(
    factory.django.DjangoModelFactory,
    metaclass=BaseMetaFactory[CorporationRoleGroup],
):
    """Generate a CorporationRoleGroup object for testing."""

    class Meta:
        model = CorporationRoleGroup
        django_get_or_create = ("id",)

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker("word")
    applies_to = "roles"
    applies_to_grantable = "grantableRoles"
    is_divisional = False
    is_locational = False


class CorporationRoleFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[CorporationRole]
):
    """Generate a CorporationRole object for testing."""

    class Meta:
        model = CorporationRole
        django_get_or_create = ("id",)

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker("word")
    description = factory.Faker("sentence")
    short_name = factory.Faker("word")


class CorporationRoleGroupMembershipFactory(
    factory.django.DjangoModelFactory,
    metaclass=BaseMetaFactory[CorporationRoleGroupMembership],
):
    """Generate a CorporationRoleGroupMembership object for testing."""

    class Meta:
        model = CorporationRoleGroupMembership

    corporation_role = factory.SubFactory(CorporationRoleFactory)
    role_group = factory.SubFactory(CorporationRoleGroupFactory)


class MetenoxMoonDrillFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[MetenoxMoonDrill]
):
    """Generate a MetenoxMoonDrill object for testing."""

    class Meta:
        model = MetenoxMoonDrill
        django_get_or_create = ("item_type",)

    item_type = factory.SubFactory(ItemTypeFactory)
    mining_cycle_time = 3600
    mining_efficiency = factory.fuzzy.FuzzyFloat(0, 1, 2)
    reagents_consumed_per_cycle = factory.fuzzy.FuzzyInteger(1, 100)


class SkillPlanFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[SkillPlan]
):
    """Generate a SkillPlan object for testing."""

    class Meta:
        model = SkillPlan
        django_get_or_create = ("id",)

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker("word")
    internal_name = factory.Faker("word")
    description = factory.Faker("sentence")


class SkillPlanMilestoneFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[SkillPlanMilestone]
):
    """Generate a SkillPlanMilestone object for testing."""

    class Meta:
        model = SkillPlanMilestone

    skill_plan = factory.SubFactory(SkillPlanFactory)
    item_type = factory.SubFactory(ItemTypeFactory)
    level = factory.fuzzy.FuzzyInteger(1, 5)


class SkillPlanSkillRequirementFactory(
    factory.django.DjangoModelFactory,
    metaclass=BaseMetaFactory[SkillPlanSkillRequirement],
):
    """Generate a SkillPlanSkillRequirement object for testing."""

    class Meta:
        model = SkillPlanSkillRequirement

    skill_plan = factory.SubFactory(SkillPlanFactory)
    item_type = factory.SubFactory(ItemTypeFactory)
    level = factory.Sequence(lambda n: n % 5 + 1)


class SovereigntyUpgradeFactory(
    factory.django.DjangoModelFactory, metaclass=BaseMetaFactory[SovereigntyUpgrade]
):
    """Generate a SovereigntyUpgrade object for testing."""

    class Meta:
        model = SovereigntyUpgrade
        django_get_or_create = ("item_type",)

    item_type = factory.SubFactory(ItemTypeFactory)
    fuel_item_type = factory.SubFactory(ItemTypeFactory)
    hourly_upkeep = factory.fuzzy.FuzzyInteger(0, 1000)
    startup_cost = factory.fuzzy.FuzzyInteger(0, 10000)
    power_production = 0
    power_allocation = factory.fuzzy.FuzzyInteger(0, 1000)
    workforce_production = 0
    workforce_allocation = factory.fuzzy.FuzzyInteger(0, 1000)
