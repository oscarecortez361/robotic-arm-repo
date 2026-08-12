#!/usr/bin/env python3

"""Simple ROS 2 practice node that publishes sample robotic-arm joint targets.

This is an educational example only. Topic names and controller interfaces must
be adapted before use with a simulator or physical robot.
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray


class ArmCommandPublisher(Node):
    def __init__(self):
        super().__init__('arm_command_publisher')
        self.publisher_ = self.create_publisher(
            Float64MultiArray,
            '/arm_joint_targets',
            10,
        )
        self.timer = self.create_timer(2.0, self.publish_target)
        self.get_logger().info('Arm command publisher started.')

    def publish_target(self):
        msg = Float64MultiArray()

        # Example six-joint target values in radians.
        # Replace these values only after verifying the target robot or simulator.
        msg.data = [0.0, -0.75, 1.0, -0.50, 0.75, 0.0]

        self.publisher_.publish(msg)
        self.get_logger().info(f'Published joint target: {list(msg.data)}')


def main(args=None):
    rclpy.init(args=args)
    node = ArmCommandPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
