# Nombre: movement_server.launch.py
# Autor: Ysolve
# Descripción: Script de lanzamiento del servidor de movimiento de ROS

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ysolve_bot_service',
            executable='movement_server',
            output='screen'
        ),
    ])