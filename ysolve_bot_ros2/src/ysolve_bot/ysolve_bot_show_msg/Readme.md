# Compialr
colcon build --packages-select ysolve_bot_show_msg
source install/setup.bash

# Ejecutar 1 de los 3
ros2 launch ysolve_bot_show_msg show_msg.launch.py
ros2 launch ysolve_bot_show_msg show_msg_param.launch.py

# Ejecutar comando con valores
ros2 launch ysolve_bot_show_msg show_msg_param.launch.py my_distancia:=2