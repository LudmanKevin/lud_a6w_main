import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.qos import QoSProfile

class TrafficLightPublisher(Node):
    def __init__(self):
        super().__init__('traffic_light_publisher')
        qos_profile = QoSProfile(depth=10, reliability=rclpy.qos.ReliabilityPolicy.RELIABLE)
        self.publisher_ = self.create_publisher(String, 'traffic_light_state', qos_profile)
        self.timer = self.create_timer(2.0, self.publish_state)
        self.states = ['Piros', 'Sárga', 'Zöld']
        self.index = 0
        self.get_logger().info("Traffic Light Publisher started.")

    def publish_state(self):
        msg = String()
        msg.data = self.states[self.index]
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')
        self.index = (self.index + 1) % len(self.states)

def main(args=None):
    rclpy.init(args=args)
    node = TrafficLightPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()