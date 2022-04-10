# Compilar
colcon build --packages-select ysolve_bot_service
source install/setup.bash
export TURTLEBOT3_MODEL=burger


# para probar
#[Terminal1]
ros2 launch turtlebot3_gazebo empty_world.launch.py

#[Terminal2]
ros2 launch ysolve_bot_service movement_server.launch.py

#[Terminal3]
ros2 service list
ros2 service call /movement custom_interface/srv/MyMoveMsg "move: 'delante'"
ros2 service call /movement custom_interface/srv/MyMoveMsg "move: 'parar'"

    # si queremos hacerlo por cliente
ros2 run ysolve_bot_service movement_client "derecha" # incluimos la direccion de giro como argumento

# fin probar


# para probar con initial pose
#[Termina2]
ros2 run ysolve_bot_service bot_position_server

#[Terminal3] Deberia poner la posicion inicial en rviz
ros2 service call /bot_position custom_interface/srv/BotPosition "move: 'initial_pose'"
