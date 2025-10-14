import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class VehicleMonitor(Node):
    def __init__(self):
        super().__init__('vehicle_monitor_node')
        self.subscription = self.create_subscription(
            String,
            'traffic_light_state',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(String, 'vehicle_action', 10)
        self.get_logger().info("Vehicle monitor node started.")

    def listener_callback(self, msg):
        light = msg.data
        action = {
            'Piros': 'Megállás',
            'Sárga': 'Lassítás',
            'Zöld': 'Elindulás'
        }.get(light, 'Ismeretlen')
        self.get_logger().info(f'Jelzőlámpa: {light} -> Reakció: {action}')

def main(args=None):
    rclpy.init(args=args)
    node = VehicleMonitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()