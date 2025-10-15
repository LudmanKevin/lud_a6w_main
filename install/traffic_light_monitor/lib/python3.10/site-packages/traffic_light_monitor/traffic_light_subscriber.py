import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TrafficLightSubscriber(Node):
    def __init__(self):
        super().__init__('traffic_light_subscriber')
        self.subscription = self.create_subscription(String, 'traffic_light_state', self.listener_callback, 10)
        self.get_logger().info("Traffic Light Subscriber started.")

    def listener_callback(self, msg):
        self.get_logger().info(f'Kapott jelzőlámpa állapot: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = TrafficLightSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()