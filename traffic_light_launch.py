from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='traffic_light_monitor',
            executable='traffic_light_publisher',
            output='screen'
        ),
        Node(
            package='traffic_light_monitor',
            executable='vehicle_monitor_node',
            output='screen'
        )
    ])