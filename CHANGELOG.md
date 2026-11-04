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

### Fixed

- Fixed `make coverage` exiting with 0 when tests failed. The reports are still created, and the target now exits with the status of the test run, or with the status of `coverage report` if the tests passed.

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
[in development]: https://github.com/Geuthur/aa-evesde-factory/compare/v0.0.2...HEAD "In Development"
