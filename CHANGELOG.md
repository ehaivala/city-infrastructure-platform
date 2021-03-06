# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Add `source_name` and `source_id` to all TrafficControl models
- `Owner` model and foreign key relation to it for all TrafficControl models
- Add management command to import operational areas (contract areas) from Helsinki WFS
- Show traffic sign icon next to `device_type` in `TrafficSignPlan` and `TrafficSignReal` admin

### Changed
- Open attachments in new tab in admin
- The `content` attribute of `AdditionalSignPlan` and `AdditionalSignReal` models are no longer
  read only in the API.
- Move general information to be the first fieldset in admin views

### Fixed
- Traffic control model admin performance issues caused by multiple foreign key choices

## [1.1.0] - 2020-09-01

### Added
- Permissions based on operational area
- `traffic_sign_type` property for `TrafficControlDeviceType`
- Added tests for Katajanokka importer
- Add traffic sign type list filter to `TrafficControlDeviceTypeAdmin`
- Allow users to authenticate to the REST API with Token
- Add a layer model and a map view to visualize data on the map
- Add REST API endpoint for `OperationalArea`
- Show admin links when clicking features on map view
- Turn map view into a React app with Material UI

### Changed
- Admin UI usability improvements
- Add `description_fi` field for `MountType`
- Improved the plan geometry generation
- Application root URL is changed to `/city-infra`
- Remove `color` attribute from `TrafficSignPlan` and `TrafficSignReal`

### Fixed
- Fixed a bug that creating `TrafficControlDeviceType` crashes when target model is specified

## [1.0.0] - 2020-07-07

First release of the City Infrastructure Platform API.

Provides an API for handling and storing common Traffic Control entities, such as TrafficSigns and RoadMarkings.

### Added
- Traffic Control REST API
- Traffic Control models:
  - `TrafficSignPlan` and `TrafficSignReal`
  - `AdditionalSignPlan` and `AdditionalSignReal`
  - `TrafficLightPlan` and `TrafficLightReal`
  - `RoadMarkingPlan` and `RoadMarkingReal`
  - `SignpostPlan` and `SignpostReal`
  - `BarrierPlan` and `BarrierReal`
  - `MountPlan` and `MountReal`
  - `Plan`
- SSO-login with TokenAuthentication

[unreleased]: https://github.com/City-of-Helsinki/city-infrastructure-platform/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/City-of-Helsinki/city-infrastructure-platform/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/City-of-Helsinki/city-infrastructure-platform/compare/v0.0.1...v1.0.0
