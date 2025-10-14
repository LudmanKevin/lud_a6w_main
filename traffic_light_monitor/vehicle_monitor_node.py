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
        light_state = msg.data
        action_msg = String()

        if light_state == "Piros":
            action_msg.data = "Megállás"
        elif light_state == "Sárga":
            action_msg.data = "Lassítás"
        elif light_state == "GREEN":
            action_msg.data = "Elindulás"
        else:
            action_msg.data = "UNKNOWN"

        self.publisher_.publish(action_msg)
        self.get_logger().info(f'Lámpa: {light_state} -> Reakció: {action_msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = VehicleMonitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()