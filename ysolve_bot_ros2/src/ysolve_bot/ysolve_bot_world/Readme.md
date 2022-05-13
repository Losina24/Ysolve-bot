####  export
export GAZEBO_MODEL_PATH=$HOME/Descargas/Ysolve-bot/ysolve_bot_ros2/src/ysolve_bot/ysolve_bot_world/models:$GAZEBO_MODEL_PATH
export TURTLEBOT3_MODEL=burger

####  Lanzar Mundo
ros2 launch ysolve_bot_world ysolve_bot_world.launch.py
