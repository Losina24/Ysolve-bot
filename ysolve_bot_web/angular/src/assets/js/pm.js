function moveRight() {
    selectedMovement="MOVE_RIGHT"
    let topic = new ROSLIB.Topic({
        ros: data.ros,
        name: '/cmd_vel',
        messageType: 'geometry_msgs/msg/Twist'
    })
    let message = new ROSLIB.Message({
        linear: {x: 0.2, y: 0, z: 0, },
        angular: {x: 0, y: 0, z: -0.2, },
    })
    topic.publish(message)
    //changeActionImgParam()
}

function moveLeft() {
    selectedMovement="MOVE_LEFT"
    let topic = new ROSLIB.Topic({
        ros: data.ros,
        name: '/cmd_vel',
        messageType: 'geometry_msgs/msg/Twist'
    })
    let message = new ROSLIB.Message({
        linear: {x: 0.2, y: 0, z: 0, },
        angular: {x: 0, y: 0, z: 0.2, },
    })
    topic.publish(message)
    //changeActionImgParam()
}

function moveForward() {
    selectedMovement="MOVE_UP"
    let topic = new ROSLIB.Topic({
        ros: data.ros,
        name: '/cmd_vel',
        messageType: 'geometry_msgs/msg/Twist'
    })
    let message = new ROSLIB.Message({
        linear: {x: 0.2, y: 0, z: 0, },
        angular: {x: 0, y: 0, z: 0, },
    })
    topic.publish(message)
    //changeActionImgParam()
}

function moveBack() {
    selectedMovement="MOVE_DOWN"
    let topic = new ROSLIB.Topic({
        ros: data.ros,
        name: '/cmd_vel',
        messageType: 'geometry_msgs/msg/Twist'
    })
    let message = new ROSLIB.Message({
        linear: {x: -0.2, y: 0, z: 0, },
        angular: {x: 0, y: 0, z: 0, },
    })
    topic.publish(message)
    //changeActionImgParam()
}

function moveStop() {
    alert('stop')
    selectedMovement="STOP"
    let topic = new ROSLIB.Topic({
        ros: data.ros,
        name: '/cmd_vel',
        messageType: 'geometry_msgs/msg/Twist'
    })
    let message = new ROSLIB.Message({
        linear: {x: 0, y: 0, z: 0, },
        angular: {x: 0, y: 0, z: 0, },
    })
    topic.publish(message)
    //changeActionImgParam()
}

function subscribe(){
    let topic = new ROSLIB.Topic({
        ros: data.ros,
        name: '/odom',
        messageType: 'nav_msgs/msg/Odometry'
    })

    topic.subscribe((message) => {
        console.log("message", message)
        data.position = message.pose.pose.position
            document.getElementById("positionTurtlebotX").innerText = data.position.x.toFixed(2)
            document.getElementById("positionTurtlebotY").innerText = data.position.y.toFixed(2)
            if(selectedMovement=="STOP"){
                document.getElementById("velocityTurtlebot").innerText = "0 m/s"
            } else {
                document.getElementById("velocityTurtlebot").innerText = message.twist.twist.linear.x.toFixed(2)+" m/s"
            }
    })
}

function connect(){
    alert()
    document.getElementById('stop').addEventListener('click', moveStop)

    data.rosbridge_address = document.getElementById("connAddress").value
    data.ros = new ROSLIB.Ros({
        url: data.rosbridge_address
    })
  
    // Define callbacks
    data.ros.on("connection", () => {
        data.connected = true
        console.log("Conexion con ROSBridge correcta")
        document.getElementById("connImg").src="assets/Green_Light_Icon.svg.png";
        subscribe()
    })
    data.ros.on("error", (error) => {
        console.log("Se ha producido algun error mientras se intentaba realizar la conexion")
        console.log(error)
    })
    data.ros.on("close", () => {
        data.connected = false
        document.getElementById("connImg").src="assets/Red_Light_Icon.svg.png";
        console.log("Conexion con ROSBridge cerrada")
    })
}

function disconnect(){
    data.ros.close()
    data.connected = false
    console.log('Clic en botón de desconexión')
}  