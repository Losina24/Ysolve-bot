# Ejecutar 1 DE LOS DOS MUNDOS EL QUE SEA NO LOS 2
ros2 launch ysolve_bot_world ysolve_bot_world.launch.py
ros2 launch turtlebot3_gazebo empty_world.launch.py

# ejecutar publisher script
ros2 launch ysolve_bot_publisher ysolve_bot_publisher.launch.py

ros2 launch ysolve_bot_publisher initial_pose.launch.py
