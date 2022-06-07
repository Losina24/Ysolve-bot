# Nombre: bot_position_server.py
# Autor: Ysolve
# Descripción: Script con la lógica necesaria para poder navegar hasta distintas posiciones con el robot

# Importar mensajes
from custom_interface.srv import BotPosition

#importar  biblioteca Python ROS2
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped
from rclpy.action import ActionClient
from nav2_msgs.action import NavigateToPose, FollowWaypoints, ComputePathToPose
from geometry_msgs.msg import Pose, PoseStamped
from action_msgs.msg import GoalStatus
from rclpy.qos import ReliabilityPolicy, QoSProfile


class Service(Node):

    '''
    Nodo que se encarga de ejecutarse como servidor para recibir peticiones de ros2web o la terminal

    Atributes:
        self._initial_pose_pub: Publicador de la posicion inicial
        self.__action_client: Accion del cliente para ir a una posicion
        self.follow_waypoints_client: Cliente de acciones para ir a varios puntos mediante un array
    '''

    def __init__(self):
        #constructor con el nombre del nodo
        super().__init__('bot_position_server_node') 
        # declara el objeto servicio pasando como parametros
        # tipo de mensaje
        # nombre del servicio
        # callback del servicio
        self.srv = self.create_service(BotPosition, 'bot_position', self.bot_position_service_callback)
        self._initial_pose_pub = self.create_publisher(PoseWithCovarianceStamped, 'initialpose', 1)
        self.__action_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')
        self.follow_waypoints_client = ActionClient(self, FollowWaypoints, '/FollowWaypoints')
        
    def bot_position_service_callback(self, request, response):
        '''
        Funcion callback que se ejecuta al recibir peticiones del servicio

        Atr:
            request: mensaje de peticion
        '''

        if request.move == "initial_pose":
            msg = PoseWithCovarianceStamped()
            msg.header.frame_id = 'map'
            msg.pose.pose.position.x = 0.0
            msg.pose.pose.position.y = -0.1
            msg.pose.pose.orientation.w = 1.0
            
            self.get_logger().info('Publishing  Initial Position  \n X= 0.0 \n Y=-0.1 \n W = 1.0 ')
            self._initial_pose_pub.publish(msg)
            # imprime mensaje informando del movimiento
            response.success = True

        elif request.move == "go_to_pose":
            # Crear la posicion de tipo PoseStamped (para pasar al Goal de la accion NavigateToPose)
            goal_pose = PoseStamped()
            # Header
            goal_pose.header.frame_id = 'map'
            goal_pose.header.stamp = self.get_clock().now().to_msg()
            #Pose
            goal_pose.pose.position.x = 2.2
            goal_pose.pose.position.y = -2.2
            goal_pose.pose.orientation.w = 1.0
            self.send_goal(goal_pose)
        elif request.move == "nav_to_pose_a":
            # Crear la posicion de tipo PoseStamped (para pasar al Goal de la accion NavigateToPose)
            goal_pose = PoseStamped()
            # Header
            goal_pose.header.frame_id = 'map'
            goal_pose.header.stamp = self.get_clock().now().to_msg()
            #Pose
            goal_pose.pose.position.x = 4.0
            goal_pose.pose.position.y = -0.05
            goal_pose.pose.orientation.w = 1.0
            self.send_goal(goal_pose)
        elif request.move == "nav_to_pose_b":
            # Crear la posicion de tipo PoseStamped (para pasar al Goal de la accion NavigateToPose)
            goal_pose = PoseStamped()
            # Header
            goal_pose.header.frame_id = 'map'
            goal_pose.header.stamp = self.get_clock().now().to_msg()
            #Pose
            goal_pose.pose.position.x = 6.1
            goal_pose.pose.position.y = -0.24
            goal_pose.pose.orientation.w = 1.0
            self.send_goal(goal_pose)
        elif request.move == "nav_to_pose_c":
            # Crear la posicion de tipo PoseStamped (para pasar al Goal de la accion NavigateToPose)
            goal_pose = PoseStamped()
            # Header
            goal_pose.header.frame_id = 'map'
            goal_pose.header.stamp = self.get_clock().now().to_msg()
            #Pose
            goal_pose.pose.position.x = 6.14
            goal_pose.pose.position.y = -2.48
            goal_pose.pose.orientation.w = 1.0
            self.send_goal(goal_pose)
        elif request.move == "nav_to_pose_d":
            # Crear la posicion de tipo PoseStamped (para pasar al Goal de la accion NavigateToPose)
            goal_pose = PoseStamped()
            # Header
            goal_pose.header.frame_id = 'map'
            goal_pose.header.stamp = self.get_clock().now().to_msg()
            #Pose
            goal_pose.pose.position.x = 4.38
            goal_pose.pose.position.y = -2.33
            goal_pose.pose.orientation.w = 1.0
            self.send_goal(goal_pose)
        elif request.move == "nav_to_pose_e":
            # Crear la posicion de tipo PoseStamped (para pasar al Goal de la accion NavigateToPose)
            goal_pose = PoseStamped()
            # Header
            goal_pose.header.frame_id = 'map'
            goal_pose.header.stamp = self.get_clock().now().to_msg()
            #Pose
            goal_pose.pose.position.x = 2.0
            goal_pose.pose.position.y = -2.5
            goal_pose.pose.orientation.w = 1.0
            self.send_goal(goal_pose)
        elif request.move == "nav_to_pose_f":
            # Crear la posicion de tipo PoseStamped (para pasar al Goal de la accion NavigateToPose)
            goal_pose = PoseStamped()
            # Header
            goal_pose.header.frame_id = 'map'
            goal_pose.header.stamp = self.get_clock().now().to_msg()
            #Pose
            goal_pose.pose.position.x = 0.3
            goal_pose.pose.position.y = -1.6
            goal_pose.pose.orientation.w = 1.0
            self.send_goal(goal_pose)
        elif request.move == "nav_to_pose_all":
            goal_poses = []
    
            # Crear la posicion de tipo PoseStamped (para pasar al Goal de la accion NavigateToPose)
            goal_pose = PoseStamped()
            # Header
            goal_pose.header.frame_id = 'map'
            goal_pose.header.stamp = self.get_clock().now().to_msg()
            #Pose
            goal_pose.pose.position.x = 0.0
            goal_pose.pose.position.y = -1.0
            goal_pose.pose.orientation.w = 1.0
            goal_poses.append(goal_pose)

            goal_pose = PoseStamped()
            # Header
            goal_pose.header.frame_id = 'map'
            goal_pose.header.stamp = self.get_clock().now().to_msg()
            #Pose
            goal_pose.pose.position.x = 1.2
            goal_pose.pose.position.y = -3.0
            goal_pose.pose.orientation.w = 1.0
            goal_poses.append(goal_pose)
            
            self.followWaypoints(goal_poses)
            
        elif request.move == "go_to_waypoints":
            goal_poses = []
    
            # Crear la posicion de tipo PoseStamped (para pasar al Goal de la accion NavigateToPose)
            goal_pose = PoseStamped()
            # Header
            goal_pose.header.frame_id = 'map'
            goal_pose.header.stamp = self.get_clock().now().to_msg()
            #Pose
            goal_pose.pose.position.x = 0.5
            goal_pose.pose.position.y = -1.2
            goal_pose.pose.orientation.w = 1.0
            goal_poses.append(goal_pose)

            goal_pose = PoseStamped()
            # Header
            goal_pose.header.frame_id = 'map'
            goal_pose.header.stamp = self.get_clock().now().to_msg()
            #Pose
            goal_pose.pose.position.x = 2.2
            goal_pose.pose.position.y = -2.0
            goal_pose.pose.orientation.w = 1.0
            goal_poses.append(goal_pose)
            
            self.followWaypoints(goal_poses)
        
        else:
            response.success = False

        # devuelve la respuesta
        return response
        
        
    #definimos la funcion de mandar goal
    def send_goal(self, pose):
        '''
        Funcion que ejecuta que el robot vaya solamente a 1 punto y luego se pare

        Atr:
            pose: posición a la que se dirige el robot
        '''
        self.get_logger().info('4')

        #espera a que el servidor este listo
        self.get_logger().info("Waiting for 'NavigateToPose' action server")
        while not self.__action_client.wait_for_server(timeout_sec=1.0):
            self.get_logger().info("'NavigateToPose' action server not available, waiting...")

        # crea el mensaje tipo Goal
        # y lo rellena con el argumento pose (de tipo PoseStamped)
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose = pose
        
        self.get_logger().info('Navigating to goal: ' + str(pose.pose.position.x) + ' ' +
                      str(pose.pose.position.y) + '...')
                      
        # envia el goal
        self._send_goal_future = self.__action_client.send_goal_async(goal_msg,feedback_callback=self.__feedback_callback)

        
        self.get_logger().info('Going to final position...')
        #rclpy.spin_until_future_complete(self, self._send_goal_future)

        self._send_goal_future.add_done_callback(self.__goal_response_callback)
        
    #definimos la funcion de respuesta al feedback
    def __feedback_callback(self, feedback_msg):
        self.get_logger().info('7')

        self.feedback = feedback_msg.feedback
        return
    #definimos la funcion de respuesta al goal
    def __goal_response_callback(self, future):
        self.get_logger().info('5')

        self.__goal_handle = future.result()
        if not self.__goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            self.__goal_handle.cancel_goal_async()

            #Si sale mal reiniciamos los atributos de __acion_client y __goal_handle 
            self.__reset_action()
            return

        self.get_logger().info('Goal accepted :)')

        self._get_result_future = self.__goal_handle.get_result_async()
        #rclpy.spin_until_future_complete(self, self._get_result_future)
        self._get_result_future.add_done_callback(self.__get_result_callback)
    
    #definimos la funcion de respuesta al resultado
    def __get_result_callback(self, future):
        self.get_logger().info('6')


        self.status = future.result().status
        if self.status != GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().info('Navigation failed with status code: {0}'.format(self.status))
        else:
            self.get_logger().info('Goal success!')
        
        self.__reset_action()

        #rclpy.shutdown()

    #definimos la funcion de respuesta al feedback
    def __feedback_callback(self, feedback_msg):
        self.get_logger().info('7')

        self.feedback = feedback_msg.feedback
        return
    
    #Metodo para resetear los atributos __goal_handle y __action_client
    def __reset_action(self):
        self.get_logger().info('8')

        self.__goal_handle = None
        self.__action_client = None
        
    def followWaypoints(self, poses):
        '''
        Funcion que ejecuta que el robot vaya a varios puntos mediante un array
        Atr:
            poses: array de de posiciones
        '''
        # Sends a `FollowWaypoints` action request
        self.get_logger().info("Waiting for 'FollowWaypoints' action server")
        while not self.follow_waypoints_client.wait_for_server(timeout_sec=1.0):
            self.get_logger().info("'FollowWaypoints' action server not available, waiting...")

        goal_msg = FollowWaypoints.Goal()
        goal_msg.poses = poses

        self.get_logger().info('Following ' + str(len(goal_msg.poses)) + ' goals.' + '...')
        send_goal_future = self.follow_waypoints_client.send_goal_async(goal_msg,
                                                                        self._feedbackCallback)
        rclpy.spin_until_future_complete(self, send_goal_future)
        self.goal_handle = send_goal_future.result()

        if not self.goal_handle.accepted:
            self.error('Following ' + str(len(poses)) + ' waypoints request was rejected!')
            return False

        self.result_future = self.goal_handle.get_result_async()
        return True

    def _feedbackCallback(self, msg):
        self.get_logger().info('Received action feedback message')
        self.feedback = msg.feedback
        return

def main(args=None):
    # inicializa la comunicacion ROS2
    rclpy.init(args=args)
    # creamos el nodo
    service = Service()

    try:
        #dejamos abierto el servicio
        rclpy.spin(service)
    except KeyboardInterrupt:
        service.get_logger().info('Cerrando el nodo service')
    finally:
        #destruimos el nodo
        service.destroy_node()
        #cerramos la comunicacion
        rclpy.shutdown()

#definimos el ejecutable
if __name__=='__main__':
    main()
