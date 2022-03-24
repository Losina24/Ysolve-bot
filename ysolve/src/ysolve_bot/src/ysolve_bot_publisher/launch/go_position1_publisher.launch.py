from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ysolve_bot_publisher',
            executable='position1_publisher',
            output='screen'),
    ])
