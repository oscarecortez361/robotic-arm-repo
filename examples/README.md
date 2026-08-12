# ROS 2 Practice Examples

These small Python programs demonstrate basic ROS 2 communication patterns that are useful in robotic-arm systems.

They are intentionally simple so the ROS concepts are easy to follow and modify.

## Files

### `ros2_arm_command_publisher.py`
Publishes a sample list of robotic-arm joint targets using `Float64MultiArray`.

### `ros2_joint_state_monitor.py`
Subscribes to `sensor_msgs/JointState` and prints joint names and positions as messages arrive.

## Typical ROS 2 Setup

A ROS 2 Python environment with `rclpy` and the standard ROS message packages is required.

Example workflow:

```bash
source /opt/ros/<distribution>/setup.bash
python3 ros2_arm_command_publisher.py
```

In a second terminal:

```bash
source /opt/ros/<distribution>/setup.bash
python3 ros2_joint_state_monitor.py
```

Actual topic names and controller interfaces vary by robot, simulator, ROS distribution, and configuration. These examples are educational starting points and should be adapted to the specific robotic platform before use.

## Safety

Do not connect example motion commands directly to physical industrial hardware without verifying the controller interface, joint limits, robot state, workspace, tooling, payload, and applicable safety procedures.
