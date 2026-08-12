#!/usr/bin/env python3

"""Simple ROS 2 practice node for monitoring robotic-arm joint states."""

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState


class JointStateMonitor(Node):
    def __init__(self):
        super().__init__('joint_state_monitor')
        self.subscription = self.create_subscription(
            JointState,
            '/joint_states',
            self.joint_state_callback,
            10,
        )
        self.get_logger().info('Joint state monitor started.')

    def joint_state_callback(self, msg):
        if not msg.name:
            self.get_logger().info('JointState message received with no joint names.')
            return

        joint_data = []
        for index, name in enumerate(msg.name):
            position = msg.position[index] if index < len(msg.position) else None
            joint_data.append(f'{name}: {position}')

        self.get_logger().info(' | '.join(joint_data))


def main(args=None):
    rclpy.init(args=args)
    node = JointStateMonitor()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
