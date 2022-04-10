# BUild
colcon build --packages-select ysolve_bot_subscriber
source install/setup.bash

# laucnh
ros2 launch ysolve_bot_subscriber ysolve_bot_subscriber.launch.py