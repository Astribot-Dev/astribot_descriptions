# Migration from the Earlier S1 Layout

The current repository organizes S1 and T1 models under separate robot directories. File names and model composition may differ from earlier releases; migration is not always a path-only change.

| Earlier location or use | Current location or migration action |
|---|---|
| `mjcf/astribot_s1_mjcf/` | Select the dynamic or kinematic entry under `astribot_s1/model/mjcf/robot/`. The files are not one-to-one replacements. |
| `urdf/astribot_s1_urdf/` | Select the matching component or whole-body file under `astribot_s1/model/urdf/`, then review the link and joint composition. |
| `usd/astribot_s1_usd/` | The current model layout does not provide an equivalent USD asset. Use a release that includes USD for workflows that require it. |
| Fixed-base, hand, Aloha and other named variants | Do not assume a direct equivalent. Port and validate the specific use case before switching versions. |
| S1/T1 directories from the `aos` layout | Review the T1 frame and wheel changes and the ancillary model updates listed in [CHANGELOG.md](CHANGELOG.md). |

## Model semantics

The current whole-body S1 URDF is composed differently from the earlier file with the same name. Recheck links, controllable joints, gripper mimic relationships, wheel joints and sensor frames.

Arm, head and torso effort and velocity limits differ from the earlier default release. Tool-reference offsets and end-effector parent links also changed. Model limits are simulation data, not certified physical-hardware limits. Compare the selected model files instead of relying on names alone.

For T1, review `t1.xml`, `t1_kinematic.xml`, `kinematic.xml` and `kinematic_visual.xml` together. The chassis root is at the model origin, a physical torso body is included, wheel local positions are updated and `torso_tool` is present. Local-coordinate changes do not directly describe world-coordinate motion. Validate chassis, wheel, torso, tool and sensor transforms with the consuming controller.

## Updating T1 sensor calibrations from v2.1.1 to v2.1.2

Keep using the same dynamic or kinematic model entry. For both wrists, reload the camera pose and vertical field of view from the model before using stored camera matrices or previously recorded observations. Check any application override to avoid applying a calibration correction twice.

The chassis IMU site, front lidar and rear camera now reference `chassis_base` directly. A transform previously measured relative to `physical_torso_base` is no longer the transform to use relative to `chassis_base`. Check transforms using the published entry point with your own application. To reproduce observations made with the previous calibration, pin `v2.1.1`.

## Upgrade and rollback

Keep the previous application version, model tag, environment and local modifications available while testing a new combination. Test in a separate checkout so the existing installation remains recoverable.

This is a standalone model asset release; it does not declare compatibility with a particular application release. Select an immutable model tag, fetch its Git LFS objects and run the asset checks in [README.md](README.md). Update the consuming application's pinned model reference and run its integration and acceptance tests before deployment. A moving branch is not a substitute for a tested version pair.

To roll back, restore the recorded application/model pair and environment, including its LFS payloads. The earlier public `v1.1.0` tag identifies the previous default S1 layout; that model tag alone does not establish compatibility with an arbitrary application version.
