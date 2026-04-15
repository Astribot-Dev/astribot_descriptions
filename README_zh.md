# Astribot S1 机器人描述文件

[English](README.md)

本仓库包含 Astribot S1 机器人的仿真模型文件，支持 URDF、MJCF（MuJoCo）和 USD 格式。

# 使用指引

放入astribot_simulation仓库最表层目录

## 仓库结构

```
astribot_descriptions/
├── urdf/astribot_s1_urdf/              # URDF & SDF 模型文件
│   ├── astribot_whole_body.urdf              # 全身（躯干 + 双臂）
│   ├── astribot_whole_body_with_head.urdf    # 全身 + 头部
│   ├── astribot_whole_body_with_wheel.urdf   # 全身 + 头部 + 轮式底盘
│   ├── astribot_whole_body_maniskill.urdf    # ManiSkill 版本（含夹爪）
│   ├── astribot_arm_left.urdf                # 左臂
│   ├── astribot_arm_right.urdf               # 右臂
│   ├── astribot_torso.urdf                   # 躯干
│   ├── astribot_head.urdf                    # 头部
│   ├── *.sdf                                 # SDF 格式变体
│   └── meshes/                               # 网格文件（STL、DAE、OBJ）
├── mjcf/astribot_s1_mjcf/              # MuJoCo MJCF 模型文件
│   ├── model_with_effector/
│   │   ├── astribot_s1_model_with_gripper.xml
│   │   └── astribot_s1_model_with_hand.xml
│   ├── assets/                               # MJCF 资源定义
│   └── actuators/                            # 执行器配置
└── usd/astribot_s1_usd/               # USD 格式（Isaac Sim）
```

## 机器人配置

Astribot S1 是一款移动操作机器人，具备：

- 4 自由度躯干
- 双 7 自由度手臂（共 14 自由度）
- 2 自由度头部
- 可选夹爪或灵巧手

## 参数一致性

所有 URDF、SDF 和 MJCF 文件均基于统一的参数源，确保运动学和动力学参数一致：

- **运动学限位** — 关节位置、速度、力矩限幅。所有 URDF/SDF 的 `<limit>` 标签、MJCF 的 `range` 属性、USD 的 `physics:lowerLimit`/`physics:upperLimit`（单位为度）均派生自同一权威参数源。
- **辨识动力学** — 通过物理一致性辨识获得的动力学参数（质量、质心、惯性张量）。这些参数贴合真实机器人动力学特性，可实现精确的动力学补偿，支持重力补偿/零力拖动、高精度轨迹跟踪、阻抗控制等力控功能开发，以及 Real2Sim 迁移。所有 URDF/SDF 的 `<inertial>` 标签、MJCF 的 `<inertial>` 参数、USD 的 `physics:mass`/`physics:diagonalInertia`/`physics:principalAxes` 均派生自同一参数源。
- **MJCF 动力学** — MJCF 的 `<inertial>` 参数（pos, quat, mass, diaginertia）通过 MuJoCo 的 URDF 导入工具从 URDF 动力学参数转换而来。坐标系变换和惯量对角化在转换过程中自动处理，因此数值表示不同但物理含义等价。
- **USD 动力学** — USD 的 `diagonalInertia` 和 `principalAxes` 通过对同一惯量张量进行特征值分解获得。关节限位从弧度转换为度。

> **注意：** 用于生成这些参数的 config YAML 文件为内部维护，未包含在本仓库中。权威参数值可直接从 URDF 文件中读取（如 `<limit>` 和 `<inertial>` 标签）。

## 支持格式

| 格式 | 仿真器                      | 文件路径                         |
| ---- | --------------------------- | -------------------------------- |
| URDF | ROS、PyBullet、ManiSkill 等 | `urdf/astribot_s1_urdf/*.urdf` |
| SDF  | Gazebo                      | `urdf/astribot_s1_urdf/*.sdf`  |
| MJCF | MuJoCo                      | `mjcf/astribot_s1_mjcf/`       |
| USD  | Isaac Sim                   | `usd/astribot_s1_usd/`         |

## 许可证

本项目基于 [Apache License 2.0](LICENSE) 开源协议发布。
