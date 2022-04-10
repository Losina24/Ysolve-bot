const express = require("express");
const ROSLIB = require("roslib");

const app = express();
const port = 8080;

data = {
	ros: null,
	rosbridge_address: "ws://127.0.0.1:9090/", //'ws://127.0.0.1:9090/',
	connected: false,
};

app.get("/ros/manual/connect", (req, res) => {
	console.log("PETICION PARA CONECTAR CON ROS BRIDGE");
	connect();
});

app.get("/ros/manual/disconnect", (req, res) => {
	console.log("PETICION PARA DESCONECTAR CON ROS BRIDGE");
	disconnect();
});

app.get("/ros/manual/move/forward", (req, res) => {
	console.log("MOVIENDO ROBOT HACIA DELANTE");
	moveForward();
});

app.get("/ros/manual/move/back", (req, res) => {
	console.log("MOVIENDO ROBOT HACIA ATRAS");
	moveBack();
});

app.get("/ros/manual/move/right", (req, res) => {
	console.log("MOVIENDO ROBOT HACIA LA DERECHA");
	moveRight();
});

app.get("/ros/manual/move/left", (req, res) => {
	console.log("MOVIENDO ROBOT HACIA LA IZQUIERDA");
	moveLeft();
});

app.get("/ros/manual/move/stop", (req, res) => {
	console.log("DETENIENDO EL ROBOT");
	stop();
});
app.get("/ros/automatic/:action", (req, res) => {

	console.log("NAVEGATION ROBOT");
	console.log(req.params.action);
	navigation("nav_to_pose_" + req.params.action);
});

app.listen(port, () => {
	console.log(`Example app listening on port ${port}`);
});

function subscribe() {
	let topic = new ROSLIB.Topic({
		ros: data.ros,
		name: "/odom",
		messageType: "nav_msgs/msg/Odometry",
	});

	topic.subscribe((message) => {
		console.log("message", message);
		data.position = message.pose.pose.position;
		//document.getElementById("positionTurtlebotX").innerText = data.position.x.toFixed(2)
		//document.getElementById("positionTurtlebotY").innerText = data.position.y.toFixed(2)
	});
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
}
function navigation(valor){
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

function connect() {
	data.ros = new ROSLIB.Ros({
		url: data.rosbridge_address,
	});

	// Define callbacks

	data.ros.on("connection", () => {
		data.connected = true;

		console.log("Conexion con ROSBridge correcta");

		//subscribe()
	});

	data.ros.on("error", (error) => {
		console.log(
			"Se ha producido algun error mientras se intentaba realizar la conexion"
		);

		console.log(error);
	});

	data.ros.on("close", () => {
		data.connected = false;

		console.log("Conexion con ROSBridge cerrada");
	});
}

function disconnect() {
	data.ros.close();

	data.connected = false;

	console.log("Clic en botón de desconexión");
}
