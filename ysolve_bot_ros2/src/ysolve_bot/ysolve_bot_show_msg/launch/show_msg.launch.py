from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ysolve_bot_show_msg',
            executable='show_msg', # referencia a dentro de ysolve_bot_show_msg/ysolve_bot_show_msg/show_msg.py
            output='screen'),
    ])
