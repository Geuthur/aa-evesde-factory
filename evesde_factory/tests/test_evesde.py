"""Test to ensure that the factories are working correctly."""

# Third Party
import factory

# Django
from django.apps import apps

# Alliance Auth (External Libs)
from eve_sde.models import BlueprintActivity, TypeDogma

# AA EVE SDE Factory
from evesde_factory import eve_sde
from evesde_factory.eve_sde import (
    AccountingEntryTypeFactory,
    ArchetypeFactory,
    BlueprintActivityFactory,
    BlueprintActivityMaterialFactory,
    BlueprintActivityProductFactory,
    CertificateFactory,
    CertificateRecommendedTypeFactory,
    CertificateSkillFactory,
    ConstellationFactory,
    CorporationRoleFactory,
    CorporationRoleGroupFactory,
    CorporationRoleGroupMembershipFactory,
    DogmaAttributeCategoryFactory,
    DogmaAttributeFactory,
    DogmaEffectFactory,
    DogmaUnitFactory,
    FreelanceJobSchemaFactory,
    FreelanceJobSchemaParameterFactory,
    ItemCategoryFactory,
    ItemGroupFactory,
    ItemMarketGroupFactory,
    ItemTypeFactory,
    ItemTypeMaterialsFactory,
    LandmarkFactory,
    MasteryFactory,
    MetenoxMoonDrillFactory,
    MoonFactory,
    NotificationTypeFactory,
    NPCStationFactory,
    PlanetFactory,
    PlanetResourceFactory,
    RegionFactory,
    SkillPlanFactory,
    SkillPlanMilestoneFactory,
    SkillPlanSkillRequirementFactory,
    SolarSystemFactory,
    SovereigntyUpgradeFactory,
    StarFactory,
    StargateFactory,
    StarResourceFactory,
    TypeDogmaFactory,
    TypeEffectFactory,
    TypeListCategoryFactory,
    TypeListFactory,
    TypeListGroupFactory,
    TypeListTypeFactory,
)
from evesde_factory.tests import EVESDEFactoryTestCase

# Import bookkeeping of django-eveonline-sde, not SDE data
MODELS_WITHOUT_FACTORY = {"EveSDE", "EveSDESection"}


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

    def test_can_create_planet(self):
        """Test that a planet can be created."""
        planet = PlanetFactory()
        self.assertIsNotNone(planet.id)
        self.assertIsInstance(planet.radius, int)

    def test_can_create_item_market_group(self):
        """Test that an ItemMarketGroup can be created."""
        obj = ItemMarketGroupFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_item_type_materials(self):
        """Test that an ItemTypeMaterials can be created."""
        obj = ItemTypeMaterialsFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_type_list(self):
        """Test that a TypeList can be created."""
        obj = TypeListFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_type_list_type(self):
        """Test that a TypeListType can be created."""
        obj = TypeListTypeFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_type_list_group(self):
        """Test that a TypeListGroup can be created."""
        obj = TypeListGroupFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_type_list_category(self):
        """Test that a TypeListCategory can be created."""
        obj = TypeListCategoryFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_dogma_attribute_category(self):
        """Test that a DogmaAttributeCategory can be created."""
        obj = DogmaAttributeCategoryFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_dogma_unit(self):
        """Test that a DogmaUnit can be created."""
        obj = DogmaUnitFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_dogma_attribute(self):
        """Test that a DogmaAttribute can be created."""
        obj = DogmaAttributeFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_dogma_effect(self):
        """Test that a DogmaEffect can be created."""
        obj = DogmaEffectFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_type_effect(self):
        """Test that a TypeEffect can be created."""
        obj = TypeEffectFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_type_dogma(self):
        """Test that a TypeDogma can be created."""
        obj = TypeDogmaFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_certificate(self):
        """Test that a Certificate can be created."""
        obj = CertificateFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_certificate_skill(self):
        """Test that a CertificateSkill can be created."""
        obj = CertificateSkillFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_certificate_recommended_type(self):
        """Test that a CertificateRecommendedType can be created."""
        obj = CertificateRecommendedTypeFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_mastery(self):
        """Test that a Mastery can be created."""
        obj = MasteryFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_archetype(self):
        """Test that an Archetype can be created."""
        obj = ArchetypeFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_star(self):
        """Test that a Star can be created."""
        obj = StarFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_stargate(self):
        """Test that a Stargate can be created."""
        obj = StargateFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_npc_station(self):
        """Test that an NPCStation can be created."""
        obj = NPCStationFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_planet_resource(self):
        """Test that a PlanetResource can be created."""
        obj = PlanetResourceFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_star_resource(self):
        """Test that a StarResource can be created."""
        obj = StarResourceFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_moon(self):
        """Test that a Moon can be created."""
        obj = MoonFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_landmark(self):
        """Test that a Landmark can be created."""
        obj = LandmarkFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_freelance_job_schema(self):
        """Test that a FreelanceJobSchema can be created."""
        obj = FreelanceJobSchemaFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_freelance_job_schema_parameter(self):
        """Test that a FreelanceJobSchemaParameter can be created."""
        obj = FreelanceJobSchemaParameterFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_blueprint_activity(self):
        """Test that a BlueprintActivity can be created."""
        obj = BlueprintActivityFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_blueprint_activity_product(self):
        """Test that a BlueprintActivityProduct can be created."""
        obj = BlueprintActivityProductFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_blueprint_activity_material(self):
        """Test that a BlueprintActivityMaterial can be created."""
        obj = BlueprintActivityMaterialFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_accounting_entry_type(self):
        """Test that an AccountingEntryType can be created."""
        obj = AccountingEntryTypeFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_notification_type(self):
        """Test that a NotificationType can be created."""
        obj = NotificationTypeFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_corporation_role_group(self):
        """Test that a CorporationRoleGroup can be created."""
        obj = CorporationRoleGroupFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_corporation_role(self):
        """Test that a CorporationRole can be created."""
        obj = CorporationRoleFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_corporation_role_group_membership(self):
        """Test that a CorporationRoleGroupMembership can be created."""
        obj = CorporationRoleGroupMembershipFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_metenox_moon_drill(self):
        """Test that a MetenoxMoonDrill can be created."""
        obj = MetenoxMoonDrillFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_skill_plan(self):
        """Test that a SkillPlan can be created."""
        obj = SkillPlanFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_skill_plan_milestone(self):
        """Test that a SkillPlanMilestone can be created."""
        obj = SkillPlanMilestoneFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_skill_plan_skill_requirement(self):
        """Test that a SkillPlanSkillRequirement can be created."""
        obj = SkillPlanSkillRequirementFactory()
        self.assertIsNotNone(obj.pk)

    def test_can_create_sovereignty_upgrade(self):
        """Test that a SovereigntyUpgrade can be created."""
        obj = SovereigntyUpgradeFactory()
        self.assertIsNotNone(obj.pk)

    def test_moon_is_in_solar_system_of_its_planet(self):
        """Test that a moon is placed in the solar system of its planet."""
        moon = MoonFactory()
        self.assertEqual(moon.solar_system, moon.planet.solar_system)

    def test_blueprint_activity_pk_matches_sde_format(self):
        """Test that the BlueprintActivity pk is built like the SDE import does."""
        activity = BlueprintActivityFactory(
            activity=BlueprintActivity.Activities.copying
        )
        self.assertEqual(activity.pk, f"{activity.blueprint_item_type.id}:copying")

    def test_freelance_job_schema_parameter_pk(self):
        """Test that the FreelanceJobSchemaParameter pk combines schema and key."""
        parameter = FreelanceJobSchemaParameterFactory(key="target")
        self.assertEqual(parameter.pk, f"{parameter.schema.id}:target")

    def test_can_create_several_link_rows(self):
        """Test that unique constraints on link models do not collide."""
        TypeDogmaFactory.create_batch(3)
        MasteryFactory.create_batch(3)
        BlueprintActivityMaterialFactory.create_batch(3)
        self.assertEqual(TypeDogma.objects.count(), 3)

    def test_every_sde_model_has_a_factory(self):
        """Test that every model of django-eveonline-sde has a factory."""
        factory_models = {
            obj._meta.model
            for obj in vars(eve_sde).values()
            if isinstance(obj, type)
            and issubclass(obj, factory.django.DjangoModelFactory)
            and obj._meta.model is not None
        }
        missing = sorted(
            model.__name__
            for model in apps.get_app_config("eve_sde").get_models()
            if model not in factory_models
            and model.__name__ not in MODELS_WITHOUT_FACTORY
        )
        self.assertEqual(missing, [])

    def test_can_create_moon_without_planet(self):
        """Test that a moon can be created without a planet."""
        moon = MoonFactory(planet=None)
        self.assertIsNone(moon.planet)
        self.assertIsNone(moon.solar_system)

    def test_can_create_all_levels_for_shared_parents(self):
        """Test that levels do not collide when parents are shared."""
        item_type = ItemTypeFactory()
        certificate = CertificateFactory()
        skill_plan = SkillPlanFactory()
        MasteryFactory.create_batch(5, item_type=item_type, certificate=certificate)
        SkillPlanSkillRequirementFactory.create_batch(
            5, skill_plan=skill_plan, item_type=item_type
        )
        self.assertEqual(certificate.masteries.count(), 5)
