# AA EVE SDE Factory.<a name="aa-eve-sde-factory"></a>

Factory helpers for faster application development with EVE SDE data

______________________________________________________________________

<!-- mdformat-toc start --slug=github --maxlevel=6 --minlevel=1 -->

- [AA EVE SDE Factory.](#aa-eve-sde-factory)
  - [Features](#features)
  - [Upcoming](#upcoming)
  - [Introducing](#introducing)
  - [Contributing](#contributing)

<!-- mdformat-toc end -->

## Features<a name="features"></a>

- AllianceAuth Model Factories
  - User
    - Optional UserMainFactory with random permission assigmend
  - EveCharacter
  - EveCorporation
  - EveAlliance
- EVE SDE Model Data Generation
  - Constellation
  - ItemType
  - ItemGroup
  - ItemCategory
  - Planet
  - Region
  - SolarSystem

## Upcoming<a name="upcoming"></a>

- Remaining EVE SDE Models
- Other Utility Tools

## Introducing<a name="introducing"></a>

These factories help you quickly create realistic AllianceAuth and EVE SDE objects in tests without writing repetitive setup code. They are especially useful when you need a valid user, corporation, or item model for a fast and focused test.

```python
from evesde_factory.allianceauth import UserMainFactory
from evesde_factory.eve_sde import ItemTypeFactory


class TestEveSdeFactory(EVESDEFactoryTestCase):
    """Test the factories."""


def test_can_create_app_user_with_custom_permissions(self):
    """Create a user with a custom permission for testing."""
    user = UserMainFactory(permissions__=["yourapp.basic_access"])
    self.assertTrue(user.has_perm("yourapp.basic_access"))


def test_create_itemtype(self):
    """Create a basic EVE SDE item type for testing."""
    custom_name = "Custom Item Type"
    item_type = ItemTypeFactory(name=custom_name)
    self.assertEqual(item_type.name, custom_name)
```

## Contributing<a name="contributing"></a>

You want to improve the project?
Please ensure you read the [Contribution Guidelines]

<!-- MD Links -->

[contribution guidelines]: https://github.com/Geuthur/aa-evesde-factory/blob/master/CONTRIBUTING.md "Contribution Guidelines"
