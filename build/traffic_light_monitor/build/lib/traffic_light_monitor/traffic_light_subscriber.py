import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time

class TrafficLightPublisher(Node):
    def __init__(self):
        super().__init__('traffic_light_publisher')
        self.subscription = self.create_subscription(String, 'traffic_light_state', self.listener_callback, 10)
        timer_period = 1.0
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.states = ["Piros", "Sárga", "Zöld"]
        self.index = 0
        self.counter = 0
        self.get_logger().info("Traffic light publisher node started.")

    def timer_callback(self):
        if self.states[self.index] == "Piros" and self.counter >= 5:
            self.index = 1
            self.counter = 0
        elif self.states[self.index] == "Sárga" and self.counter >= 2:
            self.index = 2
            self.counter = 0
        elif self.states[self.index] == "Zöld" and self.counter >= 5:
            self.index = 0
            self.counter = 0

        msg = String()
        msg.data = self.states[self.index]
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published traffic light: {msg.data}')
        self.counter += 1

def main(args=None):
    rclpy.init(args=args)
    node = TrafficLightPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()