# Astribot Robot Description Files

[English](README.md) | [简体中文](README_zh.md)

Robot description files and supporting geometry for Astribot S1 and T1.

# Usage Guide

## Repository Structure

```text
astribot_descriptions/
├── astribot_s1/
│   ├── mesh/                  # DAE, OBJ, STL and textures
│   └── model/
│       ├── mjcf/robot/
│       ├── sdf/
│       └── urdf/
├── astribot_t1/
│   ├── mesh/                  # DAE, OBJ, STL and textures
│   └── model/
│       ├── mjcf/robot/
│       ├── sdf/
│       └── urdf/
├── manifest.json
└── tools/check_assets.py
```

## Robot Configuration

This repository includes S1 and T1 descriptions. The primary whole-robot files are:

| Robot | Dynamic MJCF | Kinematic MJCF | Whole-body URDF | Whole-body SDF |
|---|---|---|---|---|
| S1 | `astribot_s1/model/mjcf/robot/s1.xml` | `astribot_s1/model/mjcf/robot/s1_kinematic.xml` | `astribot_s1/model/urdf/astribot_whole_body.urdf` | `astribot_s1/model/sdf/astribot_whole_body.sdf` |
| T1 | `astribot_t1/model/mjcf/robot/t1.xml` | `astribot_t1/model/mjcf/robot/t1_kinematic.xml` | `astribot_t1/model/urdf/astribot_whole_body.urdf` | `astribot_t1/model/sdf/astribot_whole_body.sdf` |

Each model uses relative paths to supporting files. Keep the robot directory structure intact. Included MJCF fragments such as `assets.xml` and `kinematic.xml` are not standalone entry points.

## Parameter Consistency

The files in each format are the source of the values distributed for that format and repository version. Coordinate conventions and parameter representations can differ between formats; this guide does not claim that their values are numerically interchangeable. Joint limits and frames are descriptive model data, not certified physical hardware limits.

## Formats

| Format | Included content |
|---|---|
| URDF | Robot links, joints, inertial properties and geometry references |
| SDF | Whole-body model descriptions and geometry references |
| MJCF | Dynamic and kinematic model descriptions and their included fragments |
| DAE, OBJ, STL and textures | Visual and collision geometry assets |

## License

The repository-level license is Apache License 2.0 (Apache-2.0); see [LICENSE](LICENSE). Individual assets or marks may have separate notices or terms. Follow any file-specific notice that applies. Apache-2.0 does not grant trademark rights.

## Download and Verify Assets

Model assets use Git LFS. Check out the exact tag for the repository version you need, then fetch and verify the assets:

```bash
git lfs install --local
git lfs pull
python3 tools/check_assets.py
```

`manifest.json` records the expected size and SHA-256 digest of each asset, including its Git LFS object ID where applicable. GitHub source archives may contain LFS pointer files instead of the asset payloads; use Git LFS for a complete checkout.

## Quality Checks

Automated checks validate the asset inventory and resource references, parse the distributed URDF files, and check SDF structure and references. These checks do not certify physical hardware limits or performance.

## Versions and Migration

Use files from a single repository version. Review [CHANGELOG.md](CHANGELOG.md) for changes and [MIGRATION.md](MIGRATION.md) before moving from the earlier S1 layout. Model limits and frames are not certified hardware specifications.

## Contributing and Support

Report file parsing or resource lookup issues through [GitHub Issues](https://github.com/Astribot-Dev/astribot_descriptions/issues). Include the repository tag, operating system, consuming tool and entry-point path with a minimal reproduction; remove personal paths and credentials from logs.
