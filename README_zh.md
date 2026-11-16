# Astribot 机器人模型描述文件

[English](README.md) | [简体中文](README_zh.md)

本仓库提供 Astribot S1 和 T1 的模型描述文件及配套几何资源。

# Usage Guide

## Repository Structure

```text
astribot_descriptions/
├── astribot_s1/
│   ├── mesh/                  # DAE、OBJ、STL 和纹理
│   └── model/
│       ├── mjcf/robot/
│       ├── sdf/
│       └── urdf/
├── astribot_t1/
│   ├── mesh/                  # DAE、OBJ、STL 和纹理
│   └── model/
│       ├── mjcf/robot/
│       ├── sdf/
│       └── urdf/
├── manifest.json
└── tools/check_assets.py
```

## Robot Configuration

本仓库包含 S1 和 T1 描述文件。主要整机文件如下：

| 机型 | 动态 MJCF | 运动学 MJCF | 整机 URDF | 整机 SDF |
|---|---|---|---|---|
| S1 | `astribot_s1/model/mjcf/robot/s1.xml` | `astribot_s1/model/mjcf/robot/s1_kinematic.xml` | `astribot_s1/model/urdf/astribot_whole_body.urdf` | `astribot_s1/model/sdf/astribot_whole_body.sdf` |
| T1 | `astribot_t1/model/mjcf/robot/t1.xml` | `astribot_t1/model/mjcf/robot/t1_kinematic.xml` | `astribot_t1/model/urdf/astribot_whole_body.urdf` | `astribot_t1/model/sdf/astribot_whole_body.sdf` |

模型通过相对路径引用配套文件，请保留机型目录结构。`assets.xml`、`kinematic.xml` 等 MJCF 片段不能作为独立入口使用。

## Parameter Consistency

各格式文件记录了该格式和仓库版本所发布的参数。不同格式的坐标约定和参数表示方式可能不同，本指南不声称这些数值可以直接互换。关节限位和坐标系是模型描述数据，不是经认证的真实硬件限值。

## Formats

| 格式 | 文件内容 |
|---|---|
| URDF | 机器人连杆、关节、惯性属性和几何资源引用 |
| SDF | 整机模型描述和几何资源引用 |
| MJCF | 动态与运动学模型描述及其引用片段 |
| DAE、OBJ、STL 和纹理 | 外观与碰撞几何资源 |

## License

仓库级许可证为 Apache License 2.0（Apache-2.0），详见 [LICENSE](LICENSE)。个别资源或标识可能有单独声明或许可条款；如适用，请遵循对应文件声明。Apache-2.0 不授予商标权。

## Download and Verify Assets

模型资源使用 Git LFS。请切换到所需仓库版本对应的 Tag，再获取并校验资源：

```bash
git lfs install --local
git lfs pull
python3 tools/check_assets.py
```

`manifest.json` 记录每项资源的预期大小和 SHA-256 摘要，适用时也记录 Git LFS 对象 ID。GitHub 自动生成的源码压缩包可能只包含 LFS 指针文件；完整获取资源请使用 Git LFS。

## Quality Checks

自动检查会核对资源清单和引用、解析仓库内的 URDF 文件，并检查 SDF 结构和资源引用。这些检查不构成对真实硬件限值或性能的认证。

## Versions and Migration

请使用同一仓库版本中的文件。升级前请阅读[变更记录](CHANGELOG.md)，从早期 S1 目录迁移时请阅读[迁移说明](MIGRATION.md)。模型限位和坐标系不是经认证的硬件规格。

## Contributing and Support

文件解析或资源查找问题请通过 [GitHub Issues](https://github.com/Astribot-Dev/astribot_descriptions/issues) 报告，并提供仓库 Tag、操作系统、使用工具、入口路径和最小复现步骤；提交日志前请移除个人路径和凭据。
