# Changelog

This file records changes to the model files and repository tooling. Published releases are identified by immutable version tags.

## v2.1.1

This version distributes standalone S1/T1 model assets under Apache-2.0. Its scope does not include an integrated host release or a tested combination of other repositories.

### Added

- Separate S1 and T1 model directories with dynamic and kinematic MJCF entry points.
- An asset manifest with file sizes, SHA-256 digests and Git LFS object IDs where applicable.
- English and Chinese usage guides, migration notes and an asset validation tool.

### Changed

- Align the T1 MJCF chassis frame with the model root and add the `physical_torso_base` body at a 56.2 mm local offset.
- Update T1 wheel local positions and add the `torso_tool` site in the dynamic and kinematic MJCF fragments.
- Replace unavailable generation instructions in URDF and SDF comments without changing the model structure or parameters.

### Fixed

- Remove an unresolved material-library reference and its material assignment from the optional `opened_gripper.obj` mesh. Vertex, normal, face and grouping data are unchanged; loaders use their default material appearance. The supported model entry points do not reference this optional mesh.

### Compatibility

- The directory layout and model composition differ from the earlier S1 release. Review [MIGRATION.md](MIGRATION.md), pin the model version and validate it with the consuming application before upgrading.
