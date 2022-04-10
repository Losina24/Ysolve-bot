# Ejecutar Bag Files
[Terminal1]
export GAZEBO_MODEL_PATH=$HOME/Escritorio/ysolve_bot/src/ysolve_bot/ysolve_bot_world/models:$GAZEBO_MODEL_PATH
ros2 launch ysolve_bot_nav2_system ysolve_bot_sim_nav2.launch.py use_sim_time:=True

[Terminal2] # 1 de de los 2
ros2 run ysolve_bot_service movement_server
ros2 run ysolve_bot_service bot_position_server

# para bot_position_server
[Terminal3] ros2 bag record nombreDelNodo
ros2 bag record odom

[Terminal4]
ros2 service call /bot_position custom_interface/srv/BotPosition "move: 'initial_pose'"
ros2 service call /bot_position custom_interface/srv/BotPosition "move: 'go_to_pose'"
ros2 service call /bot_position custom_interface/srv/BotPosition "move: 'go_to_waypoints'"

# para movement_server
[Terminal3] ros2 bag record nombreDelNodo
ros2 bag record cmd_vel

[Terminal4]
ros2 service call /movement custom_interface/srv/MyMoveMsg "move: 'derecha'"
ros2 service call /movement custom_interface/srv/MyMoveMsg "move: 'izquierda'"
ros2 service call /movement custom_interface/srv/MyMoveMsg "move: 'delante'"
ros2 service call /movement custom_interface/srv/MyMoveMsg "move: 'atras'"
ros2 service call /movement custom_interface/srv/MyMoveMsg "move: 'parar'"

[TerminalAny]
ros2 run plotjuggler plotjuggler

