const express = require("express");
const ROSLIB = require("roslib");
const cors = require("cors");
const app = express();
app.use(cors());

const port = 8080;
positionX = 0.0
positionY = 0.0
speed = 0.0

data = {
    ros: null,
    rosbridge_address: "ws://192.168.0.120:9090/", //'ws://127.0.0.1:9090/',
    connected: false,
};

app.get("/ros/manual/connect", async(req, res) => {
    console.log("PETICION PARA CONECTAR CON ROS BRIDGE");
    let connRes = await connect();
    if (connRes) {
        res.send({ http: 200, message: "Connected succesfully" })
    }
});

app.get("/ros/manual/disconnect", (req, res) => {
    console.log("PETICION PARA DESCONECTAR CON ROS BRIDGE");
    disconnect();
});

app.get("/ros/manual/move/forward", async(req, res) => {
    console.log("MOVIENDO ROBOT HACIA DELANTE");
    res.send(await moveForward())
});

app.get("/ros/manual/move/back", async(req, res) => {
    console.log("MOVIENDO ROBOT HACIA ATRAS");
    res.send(await moveBack())
});

app.get("/ros/manual/move/right", async(req, res) => {
    console.log("MOVIENDO ROBOT HACIA LA DERECHA");
    res.send(await moveRight())
});

app.get("/ros/manual/move/left", async(req, res) => {
    console.log("MOVIENDO ROBOT HACIA LA IZQUIERDA");
    res.send(await moveLeft())
});

app.get("/ros/manual/move/stop", async(req, res) => {
    console.log("DETENIENDO EL ROBOT");
    res.send(await stop())
});
app.get("/ros/automatic/:action", (req, res) => {

    console.log("NAVEGATION ROBOT");
    console.log(req.params.action);
    navigation("nav_to_pose_" + req.params.action);
});

app.get('/ros/params', (req, res) => {
    console.log("OBTENIENDO LOS PARAMETROS DEL ROBOT")
    res.status(200).send({
        http: 200,
        message: "OBTENIENDO LOS PARAMETROS DEL ROBOT",
        result: { "positionX": positionX, "positionY": positionY, "speed": speed }
    })
})

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`);
});

function subscribe() {
    let topic = new ROSLIB.Topic({
        ros: data.ros,
        name: '/odom',
        messageType: 'nav_msgs/msg/Odometry'
    })

    topic.subscribe((message) => {
        data.position = message.pose.pose.position
        positionX = data.position.x.toFixed(2)
        positionY = data.position.y.toFixed(2)
        speed = message.twist.twist.linear.x.toFixed(2)
    })
}

function moveRight() {
    selectedMovement = "MOVE_RIGHT";

    let topic = new ROSLIB.Topic({
        ros: data.ros,

        name: "/cmd_vel",

        messageType: "geometry_msgs/msg/Twist",
    });

    let message = new ROSLIB.Message({
        linear: { x: 0.2, y: 0, z: 0 },

        angular: { x: 0, y: 0, z: -0.2 },
    });

    topic.publish(message);
    return { http: 200, message: "Published succesfully" }
}

function moveLeft() {
    selectedMovement = "MOVE_LEFT";

    let topic = new ROSLIB.Topic({
        ros: data.ros,

        name: "/cmd_vel",

        messageType: "geometry_msgs/msg/Twist",
    });

    let message = new ROSLIB.Message({
        linear: { x: 0.2, y: 0, z: 0 },

        angular: { x: 0, y: 0, z: 0.2 },
    });

    topic.publish(message);
    return { http: 200, message: "Published succesfully" }
}

function moveForward() {
    selectedMovement = "MOVE_UP";

    let topic = new ROSLIB.Topic({
        ros: data.ros,

        name: "/cmd_vel",

        messageType: "geometry_msgs/msg/Twist",
    });

    let message = new ROSLIB.Message({
        linear: { x: 0.2, y: 0, z: 0 },

        angular: { x: 0, y: 0, z: 0 },
    });

    topic.publish(message);
    return { http: 200, message: "Published succesfully" }
}

function moveBack() {
    selectedMovement = "MOVE_DOWN";

    let topic = new ROSLIB.Topic({
        ros: data.ros,

        name: "/cmd_vel",

        messageType: "geometry_msgs/msg/Twist",
    });

    let message = new ROSLIB.Message({
        linear: { x: -0.2, y: 0, z: 0 },

        angular: { x: 0, y: 0, z: 0 },
    });

    topic.publish(message);
    return { http: 200, message: "Published succesfully" }
}

function stop() {
    selectedMovement = "STOP";

    let topic = new ROSLIB.Topic({
        ros: data.ros,

        name: "/cmd_vel",

        messageType: "geometry_msgs/msg/Twist",
    });

    let message = new ROSLIB.Message({
        linear: { x: 0, y: 0, z: 0 },

        angular: { x: 0, y: 0, z: 0 },
    });

    topic.publish(message);
    return { http: 200, message: "Published succesfully" }
}

function navigation(valor) {
    data.service_busy = true
    data.service_response = ''

    let service = new ROSLIB.Service({
        ros: data.ros,
        name: '/bot_position',
        serviceType: 'custom_interface/srv/BotPosition'
    })

    let request = new ROSLIB.ServiceRequest({
        move: valor
    })

    console.log(valor)
    service.callService(request, (result) => {
        data.service_busy = false
        data.service_response = JSON.stringify(result)
    }, (error) => {
        data.service_busy = false
        console.error(error)
    })
}

async function connect() {
    return new Promise((resolve, reject) => {
        console.log("*** VAMOS A CONECTAR CON EL ROBOT ***");

        data.ros = new ROSLIB.Ros({
            url: data.rosbridge_address,
        });

        // Define callbacks

        data.ros.on("connection", () => {
            data.connected = true;

            console.log("Conexion con ROSBridge correcta");

            subscribe()
            resolve(true)
        });

        data.ros.on("error", (error) => {
            console.log(
                "Se ha producido algun error mientras se intentaba realizar la conexion"
            );

            console.log(error);
            reject(false)
        });

        data.ros.on("close", () => {
            data.connected = false;

            console.log("Conexion con ROSBridge cerrada");
            reject(false)
        });
    });

}

function disconnect() {
    data.ros.close();

    data.connected = false;

    console.log("Clic en botón de desconexión");
}