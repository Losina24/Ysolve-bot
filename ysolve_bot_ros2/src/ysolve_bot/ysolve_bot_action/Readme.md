# colcon
colcon build --packages-select ysolve_bot_action

# launch
[Terminal1]
ros2 launch ysolve_bot_action action_server.launch.py
[Terminal2]
ros2 action list

# para probar
[Terminal1]
ros2 launch turtlebot3_gazebo empty_world.launch.py
[Terminal2]
ros2 launch ysolve_bot_action action_server.launch.py
[Terminal3]
ros2 launch ysolve_bot_action action_client.launch.py


