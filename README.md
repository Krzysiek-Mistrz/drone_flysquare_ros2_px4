# drone_fly_square

**drone_fly_square** is a ROS 2 Python package that commands a PX4 drone to fly in a square pattern using Gazebo SITL and micro-ROS.

## Overview

This package provides:
- A ROS 2 node (`drone_fly_square`) that publishes setpoints to guide the drone.
- A launch file (`x500.launch.py`) that:
  - Builds and runs PX4 SITL (`gz_x500`).
  - Starts a Micro XRCE Agent to bridge micro-ROS.
  - Launches the square‐flight node.

## Prerequisites

- Ubuntu 22.04  
- ROS 2 (Humble) with desktop and Gazebo support  
- PX4-Autopilot source (tested on `HEAD` of `master`)  
- [Micro XRCE Agent](https://micro.ros.org/) installed  
- Python 3.8+ and `colcon`  

## Installation

1. Clone this repo into your ROS 2 workspace:
   ```
   cd ~/your_ros2_ws/src
   git clone git@github.com:Krzysiek-Mistrz/drone_flysquare_ros2_px4.git
   ```
2. Install dependencies:
   ```
   cd ~/your_ros2_ws
   rosdep install --from-paths src --ignore-src -r -y
   ```

## Build

```
cd ~/your_ros2_ws
colcon build --packages-select drone_fly_square
source install/setup.bash
```

## Usage

1. Ensure PX4-Autopilot is present and built:
   ```
   cd ~/PX4-Autopilot
   make px4_sitl
   ```
2. Launch the square‐flight scenario:
   ```
   ros2 launch drone_fly_square x500.launch.py
   ```
   This runs:
   - `make px4_sitl gz_x500` in the PX4 folder
   - `MicroXRCEAgent udp4 -p 8888`
   - `drone_fly_square` node

3. Watch Gazebo and topic output. The drone will take off and fly a square.

## Package Structure

```
simple_flight/
├── launch/
│   └── x500.launch.py
├── resource/
│   └── drone_fly_square
├── drone_fly_square/
│   └── drone_fly_square.py   # main node script
├── package.xml
└── setup.py
```

## Testing

```
cd ~/your_ros2_ws
colcon test --packages-select drone_fly_square
colcon test-result --verbose
```

## Licensing

GNU GPL v3 @ Krzychu 2025