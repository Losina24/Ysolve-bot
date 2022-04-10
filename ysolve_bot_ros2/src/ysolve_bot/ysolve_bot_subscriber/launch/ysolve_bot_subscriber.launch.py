from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ysolve_bot_subscriber', # referencia al paquete
            executable='ysolve_bot_odom_subscriber', # referencia al script
            output='screen'),
    ])
