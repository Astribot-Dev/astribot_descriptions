# 🤖 **Simulation Model Files** | Description and Usage

This document describes the simulation model files used in the Astribot project for robot control and simulation.

---

## 📦 Overview

The simulation model files define the physical and logical properties of the Astribot robot in a simulated environment. These files are essential for accurate simulation and control testing.

---

## 🖥️ File Structure

- **URDF Files**: Define the robot's physical structure, including links and joints.
- **SDF Files**: Describe the robot's properties in Gazebo simulation.
- **Configuration Files**: Include parameters for controllers, sensors, and other components.

---

## 🚀 Usage

### 1. Load the Model in Simulation
- Ensure the model files are placed in the correct directory (`<your_path>/astribot_simulation/astribot_descriptions`).
- Launch the simulation environment (e.g., mujoco) and load the model.

### 2. Modify Model Parameters
- Edit the URDF/SDF files to adjust the robot's properties (e.g., mass, dimensions).
- Update configuration files to change controller settings or sensor configurations.

### 3. Test and Validate
- Run the simulation and validate the robot's behavior against expected results.
- Debug any discrepancies by reviewing the model files and simulation logs.

---

## 📝 Notes
- Always back up the original model files before making modifications.
- Refer to the [ROS documentation](http://wiki.ros.org/urdf) for detailed guidance on URDF and SDF file syntax.
