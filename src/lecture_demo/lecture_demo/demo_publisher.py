#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class DemoPublisher(Node):
    def __init__(self):
        super().__init__("demo_publisher")
        self._publisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 1)
        timer_period = 0.05  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.linear.y = 0.0
        msg.linear.z = 0.0
        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = 1.0

        self._publisher.publish(msg)
        self.get_logger().info("Publishing twist")


def main(args=None):
    rclpy.init(args=args)

    demo_publisher = DemoPublisher()

    try:
        rclpy.spin(demo_publisher)
    except KeyboardInterrupt:
        pass
    finally:
        demo_publisher.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
