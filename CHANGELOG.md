# Changelog

## [In Development] - Unreleased

<!--
> [!NOTE]
>

> [!TIP]
>

> [!IMPORTANT]
>

> [!WARNING]
>

> [!CAUTION]
>

Section Order:

### Added
### Fixed
### Changed
### Removed
-->

<!-- Your changes go here -->

### Added

- Factories for all data models of `django-eveonline-sde` 1.0.0 (map, types, dogma, certificates, industry, freelance, misc and sovereignty models)
- Test that fails when a `django-eveonline-sde` model has no factory

### Changed

- Require `django-eveonline-sde>=1,<2` (see its README for the `modeltranslation` setup); the test settings add `modeltranslation` accordingly

### Fixed

- `ItemTypeFactory.mass` generates a float instead of a `Decimal`, `PlanetFactory.radius` an integer instead of a float, matching the model fields

## [0.0.3] - 2026-11-05

### Fixed

- `add_permission_to_user` now grants all given permissions. Before, the `return` sat inside the loop, so only the first permission was added.
- `UserFactory` now appends a running number to the generated `username`. Before, a random name could match an existing user (e.g. the superuser of `AuthTestCase`) through `django_get_or_create`, which made permission tests fail randomly. Explicitly passed usernames still use `get_or_create`.
- Fixed `make coverage` exiting with 0 when tests failed. The reports are still created, and the target now exits with the status of the test run, or with the status of `coverage report` if the tests passed.

### Changed

- `__operations__` now lists the public `GetStatus` operation instead of an empty list, which makes `esi.client` raise an `AttributeError` with `DEBUG=False`

## [0.0.2] - 2026-09-10

### Fixed

- README.md introduction example

### Added

- ItemType Custom Name Test

## [0.0.1] - 2026-09-10

### Added

- AllianceAuth Model Factories
  - User
    - Optional with random permission assigmend
  - EveCharacter
  - EveCorporation
  - EveAlliance
- EVE SDE Model Factories
  - Constellation
  - ItemType
  - ItemGroup
  - ItemCategory
  - Planet
  - Region
  - SolarSystem

<!-- Links -->

[0.0.1]: https://github.com/Geuthur/aa-evesde-factory/compare/v...v0.0.1 "v0.0.1"
[0.0.2]: https://github.com/Geuthur/aa-evesde-factory/compare/v0.0.1...v0.0.2 "v0.0.2"
[0.0.3]: https://github.com/Geuthur/aa-evesde-factory/compare/v0.0.2...v0.0.3 "v0.0.3"
[in development]: https://github.com/Geuthur/aa-evesde-factory/compare/v0.0.3...HEAD "In Development"
