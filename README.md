# **MultiBot by Ysolve**
Este repositorio contiene el software utilizado para el funcionamiento del **MultiBot by Ysolve** (nos referiremos a él como YsolveBot en el resto de la documentación), un robot terrestre modular pensado para ser fácilmente integrable con distintos algoritmos de IA para su uso en diversos escenarios tales como: detección de incendios, análisis de cultivos, detección de gases peligrosos, grabación a distancia, reconocimiento del terreno, etc. Además, este repositorio también contiene aplicación web utilizada para poder controlar el YsolveBot de forma remota.

A continuación se describirán las funcionalidades de ambas partes del proyecto, así como un manual de uso.

# **Contenido**
- [**Proyecto**](#multibot-by-ysolve)
- [**Contenido**](#contenido)
- [**ROS2**](#ros2)
    - [**Requisitos previos**](#requisitos-previos)
    - [**Empezando**](#empezando)
    - [**Estructura del proyecto**](#estructura-del-proyecto)
    - [**Paquetes**](#paquetes)
- [**Web**](#web)
    - [**Requerimientos previos**](#requerimientos-previos)
    - [**Comenzando**](#comenzando)
    - [**Estructura de la aplicación**](#estructura-de-la-aplicación)
    - [**Funcionalidades**](#funcionalidades)
- [**Licencia**](#licencia)

# **ROS2**
Para desarrollar el YsolveBot utilizamos ***ROS2*** como framework o conjunto de herramientas para implementar distintas funcionalidades tales como la ***navegación manual***, la ***navegación autónoma***, la ***conexión entre el robot y la web***, el ***envío de ordenes***, etc. 

## **Requisitos previos**
Para el enterno y la programación del robot, se ha obtado por utilizar las librerías de **turtlebot3**, una plataforma estándard de robótica, muy versátil e interesante [Single-Page applications](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/)

## **Empezando**
1. Clonar el repositorio

```bash
https://github.com/Losina24/Ysolve-bot.git
```

2. Instalar los paquetes

```bash
cd <path-to-directory>/Ysolve-bot/ysolve_bot_ros2
npm install
```

## **Estructura del proyecto**
```
ysolve_bot_ros2/
    └── src/
        ├── ysolve_bot/
        │   ├── bag_files/
        │   │   ├── ros2_bag_bot_position_server/
        │   │   ├── ros2_bag_movement_server/
        │   │   ├── ros2_bag_odom_bot_position_server/
        │   │   └── ros2_bag_odom_bot_position_server(Prueba2)/
        │   ├── custom_interface/
        │   │   ├── action/
        │   │   ├── msg/
        │   │   └── srv/
        │   ├── ysolve_bot/
        │   ├── ysolve_bot_action/
        │   │   ├── launch/
        │   │   ├── resource/
        │   │   ├── test/
        │   │   ├── ysolve_bot_action/
        │   │   ├── setup.cfg/
        │   │   └── setup.py/   
        │   ├── ysolve_bot_nav2_system/
        │   │   ├── launch/
        │   │   ├── resource/
        │   │   ├── test/
        │   │   ├── ysolve_nav2_system/
        │   │   ├── setup.cfg/
        │   │   └── setup.py/  
        │   ├── ysolve_bot_publisher/
        │   │   ├── launch/
        │   │   ├── resource/
        │   │   ├── test/
        │   │   ├── ysolve_bot_publisher/
        │   │   ├── setup.cfg/
        │   │   └── setup.py/ 
        │   ├── ysolve_bot_service/
        │   │   ├── launch/
        │   │   ├── resource/
        │   │   ├── test/
        │   │   ├── ysolve_bot_service/
        │   │   ├── setup.cfg/
        │   │   └── setup.py/ 
        │   ├── ysolve_bot_show_msg/
        │   │   ├── launch/
        │   │   ├── resource/
        │   │   ├── test/
        │   │   ├── ysolve_bot_show_msg/
        │   │   ├── setup.cfg/
        │   │   └── setup.py/ 
        │   ├── ysolve_bot_subscriber/
        │   │   ├── launch/
        │   │   ├── resource/
        │   │   ├── test/
        │   │   ├── ysolve_bot_subscriber/
        │   │   ├── setup.cfg/
        │   │   └── setup.py/ 
        │   └── ysolve_bot_world/
        │   │   ├── include/
        │   │   ├── launch/
        │   │   ├── map/
        │   │   ├── models/
        │   │   ├── src/
        │   │   └── world/ 
        └── turtlebot3_simulations/
```

## **Paquetes**

### turtlebot3_simulations
Paquete importado directamente desde el repositorio de turtlebot3 de GitHub [Single-Page applications](https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git). Tiene las librerías necesarias para poder programar, controlar y emular (gazebo) el robot.

### bag_files

**Ejecutar Bag Files**
[Terminal1]
```
export GAZEBO_MODEL_PATH=$HOME/Escritorio/ysolve_bot/src/ysolve_bot/ysolve_bot_world/models:$GAZEBO_MODEL_PATH
ros2 launch ysolve_bot_nav2_system ysolve_bot_sim_nav2.launch.py use_sim_time:=True
```

[Terminal2] # 1 de de los 2
```
ros2 run ysolve_bot_service movement_server
ros2 run ysolve_bot_service bot_position_server
```

**Para bot_position_server**
[Terminal3] 
```
ros2 bag record nombreDelNodo
ros2 bag record odom
```

[Terminal4]
```
ros2 service call /bot_position custom_interface/srv/BotPosition "move: 'initial_pose'"
ros2 service call /bot_position custom_interface/srv/BotPosition "move: 'go_to_pose'"
ros2 service call /bot_position custom_interface/srv/BotPosition "move: 'go_to_waypoints'"
```

**Para movement_server**
[Terminal3] 
```
ros2 bag record nombreDelNodo
ros2 bag record cmd_vel
```

[Terminal4]
```
ros2 service call /movement custom_interface/srv/MyMoveMsg "move: 'derecha'"
ros2 service call /movement custom_interface/srv/MyMoveMsg "move: 'izquierda'"
ros2 service call /movement custom_interface/srv/MyMoveMsg "move: 'delante'"
ros2 service call /movement custom_interface/srv/MyMoveMsg "move: 'atras'"
ros2 service call /movement custom_interface/srv/MyMoveMsg "move: 'parar'"
```

[TerminalAny]
```
ros2 run plotjuggler plotjuggler
```

### custom_interface

**Para mostrar lo del servicio conectado con el paquete ysolve_bot_service**
```
ros2 interface show custom_interface/srv/MyMoveMsg
```

### ysolve_bot_action

**colcon**
```
colcon build --packages-select ysolve_bot_action
```

**launch**
[Terminal1]
```
ros2 launch ysolve_bot_action action_server.launch.py
```
[Terminal2]
```
ros2 action list
```

**Para probar**
[Terminal1]
```
ros2 launch turtlebot3_gazebo empty_world.launch.py
```
[Terminal2]
```
ros2 launch ysolve_bot_action action_server.launch.py
```
[Terminal3]
```
ros2 launch ysolve_bot_action action_client.launch.py
```

### ysolve_bot_nav2_system

Paquete de control de la navegación del turtlebot.

**export**
```
export GAZEBO_MODEL_PATH=$HOME/Escritorio/ysolve_bot/src/ysolve_bot/ysolve_bot_world/models:$GAZEBO_MODEL_PATH
```

**Lanzar Mundo**
```
ros2 launch ysolve_bot_world ysolve_bot_world.launch.py
```

**Si sale el error file map yalm lo que hay que hacer es en el launch.py en vez de nav2_params.yalm cambiar a my_nav2_params.yalm para que no detecte el archivo y se pueda lanzar**
**Lanzar NAV**
```
ros2 launch ysolve_bot_nav2_system ysolve_bot_nav2_system.launch.py
```

**Cargar mapa**
```
ros2 service call /map_server/load_map nav2_msgs/srv/LoadMap "{map_url: $HOME/Escritorio/ysolve_bot/src/ysolve_bot/ysolve_bot_nav2_system/config/ysolve_bot_map.yaml}"
```

**initial pose**
```
ros2 run ysolve_bot_nav2_system initial_pose_pub
```

**Ejecutar**

**Luego de abrirlo esperar unos minutos a que se abra Gazebo y se configure todo. Luego darle a 2D Pose estimate, situarlo donde esta el robot y darle a navigation goal**
```
export GAZEBO_MODEL_PATH=$HOME/Escritorio/ysolve_bot/src/ysolve_bot/ysolve_bot_world/models:$GAZEBO_MODEL_PATH
ros2 launch ysolve_bot_nav2_system ysolve_bot_sim_nav2.launch.py use_sim_time:=True
```

### ysolve_bot_publisher

Se encarga de la publicación de datos relevantes del robot: posición, velocidad angular...

**Ejecutar 1 de los dos mundos. Nunca los dos a la vez**
```
ros2 launch ysolve_bot_world ysolve_bot_world.launch.py
ros2 launch turtlebot3_gazebo empty_world.launch.py
```

**Ejecutar publisher script**
```
ros2 launch ysolve_bot_publisher ysolve_bot_publisher.launch.py
ros2 launch ysolve_bot_publisher initial_pose.launch.py
```

### ysolve_bot_service
**Compilar**
```
colcon build --packages-select ysolve_bot_service
source install/setup.bash
export TURTLEBOT3_MODEL=burger
```

**Para probar**
[Terminal1]
```
ros2 launch turtlebot3_gazebo empty_world.launch.py
```

[Terminal2]
```
ros2 launch ysolve_bot_service movement_server.launch.py
```

[Terminal3]
```
ros2 service list
ros2 service call /movement custom_interface/srv/MyMoveMsg "move: 'delante'"
ros2 service call /movement custom_interface/srv/MyMoveMsg "move: 'parar'"
```

**Si queremos hacerlo por cliente**
```
ros2 run ysolve_bot_service movement_client "derecha" # incluimos la direccion de giro como argumento
```

**Para probar con initial pose**
[Termina2]
```
ros2 run ysolve_bot_service bot_position_server
```

[Terminal3] Deberia poner la posicion inicial en rviz
```
ros2 service call /bot_position custom_interface/srv/BotPosition "move: 'initial_pose'"
```

### ysolve_bot_show_msg

Este paquete se encarga de controlar los mensajes relativos con el robot; ya sea la posición, orientación...

**Compialar**
```
colcon build --packages-select ysolve_bot_show_msg
source install/setup.bash
```

**Ejecutar 1 de los 3**
```
ros2 launch ysolve_bot_show_msg show_msg.launch.py
ros2 launch ysolve_bot_show_msg show_msg_param.launch.py
```

**Ejecutar comando con valores**
```
ros2 launch ysolve_bot_show_msg show_msg_param.launch.py my_distancia:=2
```

### ysolve_bot_subscriber
**Build**
```
colcon build --packages-select ysolve_bot_subscriber
source install/setup.bash
```

**launch**
```
ros2 launch ysolve_bot_subscriber ysolve_bot_subscriber.launch.py
```

### ysolve_bot_world
Se encarga de abrir un entorno de simulación de turtlebot en un mapa en Gazebo.

**export**
```
export GAZEBO_MODEL_PATH=$HOME/Documentos/Ysolve-bot/ysolve_bot_ros2/src/ysolve_bot/ysolve_bot_world/models:$GAZEBO_MODEL_PATH
export TURTLEBOT3_MODEL=burger
```

**Lanzar Mundo**
```
ros2 launch ysolve_bot_world ysolve_bot_world.launch.py
```


# **Web**
La web cumple dos propósitos: dar a conocer el producto a nuevos clientes y servir como interfaz gráfica del robot. Con esto en mente, se ha divido en dos partes, la **landing page** y el **dashboard**.

## **Requerimientos previos**
Esta aplicación web ha sido desarrollada utilizando **Angular 12**, un framework que permite la creación de [Single-Page applications](https://es.wikipedia.org/wiki/Single-page_application) y la división de los elementos del frontend en componentes reutilizables. Además, se ha utilizado la libreri **Anime.js** para animar elementos de la interfaz gráfica y **Three.js** para implementar un motor gráfico que nos permita mostrar renders del robot en la web. Angular utiliza *TypeScript* y *Node.js*, por tanto, para poder ejecutar el servicio se deben instalar los siguientes paquetes:

- [Node.js](https://nodejs.org/en/download/)
- Angular:
```js
npm install -g @angular/cli
```

## **Comenzando**
1. Clonar el repositorio

```bash
git clone https://github.com/Losina24/Ysolve-bot
```

2. Instalar los paquetes

```bash
cd <path-to-directory>/Ysolve-bot/angular
npm install
```

3. Run Angular

```bash
ng serve --open
```

> Si el puerto 4200 ya está en uso
```bash
ng serve --port {port} --open
```

> Si quieres ejecutar el servicio sin abrir el navegador
```bash
ng serve
```

## **Estructura de la aplicación**
```
angular/
    ├── node_modules/
    └── src/
        ├── app/
        │   ├── pages/
        │   │   ├── dashboard
        │   │   └── landing-page
        │   ├── shared/
        │   │   ├── components/
        │   │   │   ├── layout/
        │   │   │   │   ├── alt-section
        │   │   │   │   ├── basic-section
        │   │   │   │   ├── feature
        │   │   │   │   ├── features-section
        │   │   │   │   ├── footer
        │   │   │   │   ├── header
        │   │   │   │   ├── main-cover
        │   │   │   │   ├── main-quote
        │   │   │   │   └── smartphone-render
        │   │   │   ├── login
        │   │   │   └── dashboard-element
        │   │   └── services/
        │   ├── app-routing.module.ts
        │   ├── app.component.html
        │   ├── app.component.scss
        │   ├── app.component.ts
        │   └── app.module.ts
        ├── assets/
        ├── enviroments/
        ├── favicon.ico
        ├── index.html
        ├── main.ts
        ├── polyfills.ts
        ├── styles.scss
        └── test.ts
```

## **Funcionalidades**

### Landing Page
La landing page es primera página que ve el usuario cuando entra. Su objetivo es mostrar las funcionalidades del producto al posible cliente. Hemos dividido esta página en distintas secciones, cada una en un componente distinto:

- **Header:** El es elemento que se muestra en la parte superior de la pantalla. Muestra el logotipo, un enlace a la página de Ysolve y un boton que abre el menú de login.
- **Main cover:** Este componente contiene la primera sección de la landing page, que muestra un título, con una imagen del robot y un call to action.
- **Main quote:** Contiene una cita que se muestra después del main cover. Sirve para separar secciones y enfatizar la calidad del producto.
- **Features section:** Esta sección contiene una imagen de la futura aplicación y una descripción de las funcionalidades del producto.
- **Basic section:** Esta sección contiene un texto básico y una imagen para acompañarlo.
- **Alt section:** Esta sección contiene un call to action que lleva a la página de Ysolve.
- **Footer:** El pie de página de la web.

### Login
Es un sencillo formulario con dos campos que permite al usuario acceder al dashboard del robot.

### Dashboard
El dashboard es la otra página implementada. Se utiliza como interfaz gráfica para comunicarse con el robot. Contiene las siguientes funcionalidades:

- **Menú de información:** Muestra una serie de etiquetas con información del robot como el nombre, la velocidad, el ángulo de giro, etc.
- **Mapa:** Es una representación visual del mundo por el cuál se mueve el robot. Tiene una serie de waypoints a los que el robot puede desplazarse desde el menú de navegación.
- **Menú de navegación:** Tiene dos modos: manual y automática. En el modo manual, se pueden enviar acciones al robot indicando la dirección en la que se debe mover. En modo automático, se le indica el punto al que quiere que se desplace.
- **Ver robot:** Es un menú activable que muestra un render del robot utilizando Three.js.
- **Ver cámara:** Es un menú activable que muestra vídeo en directo desde la cámara del robot (no implementado en el robot todavía).

 # **Licencia**
El código de este repositorio es propiedad de Ysolve.
Copyright © 2022, Ysolve.
