comandos
####  export
export GAZEBO_MODEL_PATH=$HOME/Escritorio/ysolve_bot/src/ysolve_bot/ysolve_bot_world/models:$GAZEBO_MODEL_PATH

####  Lanzar Mundo
ros2 launch ysolve_bot_world ysolve_bot_world.launch.py

####  Si sale el error file map yalm lo que hay que hacer es en el launch.py en vez de nav2_params.yalm cambiar a my_nav2_params.yalm para que no detecte el archivo y se pueda lanzar
####  Lanzar NAV
ros2 launch ysolve_bot_nav2_system ysolve_bot_nav2_system.launch.py

####  cargar mapa
ros2 service call /map_server/load_map nav2_msgs/srv/LoadMap "{map_url: $HOME/Escritorio/ysolve_bot/src/ysolve_bot/ysolve_bot_nav2_system/config/ysolve_bot_map.yaml}"

#### initial pose
ros2 run ysolve_bot_nav2_system initial_pose_pub

# EJECUTAR A PARTIR DE AQUÍ

### sistema de planificacion
### luego de abrirlo esperar unos 10 mins a que se abra el gazebo y se configure todo. Luego darle a 2D Pose estimate, situarlo donde esta el robot y luego darle a navigation goal
export GAZEBO_MODEL_PATH=$HOME/Escritorio/ysolve_bot/src/ysolve_bot/ysolve_bot_world/models:$GAZEBO_MODEL_PATH
ros2 launch ysolve_bot_nav2_system ysolve_bot_sim_nav2.launch.py use_sim_time:=True