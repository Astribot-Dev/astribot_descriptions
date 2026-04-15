# Astribot S1 Robot Description Files

[中文版](README_zh.md)

This repository contains the simulation model files for the Astribot S1 robot, including URDF, MJCF (MuJoCo), and USD formats.

# Usage Guide

Place this repository in the top-level directory of the astribot_simulation repository.

## Repository Structure

```
astribot_descriptions/
├── urdf/astribot_s1_urdf/              # URDF & SDF model files
│   ├── astribot_whole_body.urdf              # Whole body (torso + arms)
│   ├── astribot_whole_body_with_head.urdf    # Whole body + head
│   ├── astribot_whole_body_with_wheel.urdf   # Whole body + head + wheels
│   ├── astribot_whole_body_maniskill.urdf    # ManiSkill version (with grippers)
│   ├── astribot_arm_left.urdf                # Left arm only
│   ├── astribot_arm_right.urdf               # Right arm only
│   ├── astribot_torso.urdf                   # Torso only
│   ├── astribot_head.urdf                    # Head only
│   ├── *.sdf                                 # SDF format variants
│   └── meshes/                               # Mesh files (STL, DAE, OBJ)
├── mjcf/astribot_s1_mjcf/              # MuJoCo MJCF model files
│   ├── model_with_effector/
│   │   ├── astribot_s1_model_with_gripper.xml
│   │   └── astribot_s1_model_with_hand.xml
│   ├── assets/                               # MJCF asset definitions
│   └── actuators/                            # Actuator configurations
└── usd/astribot_s1_usd/               # USD format for Isaac Sim
```

## Robot Configuration

The Astribot S1 is a mobile manipulation robot with:
- 4-DOF torso
- Dual 7-DOF arms (14 DOF total)
- 2-DOF head
- Optional grippers or dexterous hands

## Parameter Consistency

All URDF, SDF, and MJCF files share the same kinematic and dynamics parameters from a single source of truth:

- **Kinematic limits** — Joint position, velocity, and effort limits. All URDF/SDF `<limit>` tags, MJCF `range` attributes, and USD `physics:lowerLimit`/`physics:upperLimit` (in degrees) are derived from the same authoritative source.
- **Identified dynamics** — Dynamics parameters (mass, center of mass, inertia tensor) obtained through physically-consistent identification on the real robot. These parameters closely match the actual robot dynamics, enabling accurate dynamics compensation for force-control applications such as gravity compensation / zero-force dragging, high-precision trajectory tracking, impedance control, and real-to-sim (Real2Sim) transfer. All URDF/SDF `<inertial>` tags, MJCF `<inertial>` parameters, and USD `physics:mass`/`physics:diagonalInertia`/`physics:principalAxes` are derived from the same source.
- **MJCF dynamics** — The MJCF `<inertial>` parameters (pos, quat, mass, diaginertia) are converted from URDF dynamics via MuJoCo's URDF import tool. The coordinate frame transformation and inertia diagonalization are handled automatically during conversion, so the values differ in representation but are physically equivalent.
- **USD dynamics** — The USD `diagonalInertia` and `principalAxes` are obtained by eigenvalue decomposition of the same inertia tensor. Joint limits are converted from radians to degrees.

> **Note:** The config YAML files used to generate these parameters are maintained internally and are not included in this repository. The authoritative parameter values can be read directly from the URDF files (e.g., `<limit>` and `<inertial>` tags).

## Formats

| Format | Simulator | Files |
|--------|-----------|-------|
| URDF   | ROS, PyBullet, ManiSkill, etc. | `urdf/astribot_s1_urdf/*.urdf` |
| SDF    | Gazebo | `urdf/astribot_s1_urdf/*.sdf` |
| MJCF   | MuJoCo | `mjcf/astribot_s1_mjcf/` |
| USD    | Isaac Sim | `usd/astribot_s1_usd/` |

## License

This project is licensed under the [Apache License 2.0](LICENSE).
