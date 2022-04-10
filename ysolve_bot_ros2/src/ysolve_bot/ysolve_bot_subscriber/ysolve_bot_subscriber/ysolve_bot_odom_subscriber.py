import rclpy
# importar ROS2 python lib
from rclpy.node import Node
# importar Odometry desde la interface nav_msgs
from nav_msgs.msg import Odometry
# importar la librería de calidad del servicio para fijar las políticas de calidad
from rclpy.qos import ReliabilityPolicy, QoSProfile
import time

class Odom_Subscriber(Node):

    '''
    Nodo que crea una subscripcion al topic /odom
    Atributes:
        self.subscriber: Manejador del subscriptor
    '''

    def __init__(self):
        super().__init__('ysolve_bot_odom_subscriber')
        self.subscriber= self.create_subscription(
            Odometry,
            '/odom',
            self.listener_callback,
            QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT)) 
        # prevent unused variable warning
        self.subscriber       

    def listener_callback(self, msg):
        '''
        Callback que es llamado cuando se recibe un mensaje del topic /odom con la posición actual
        '''      
        # imprime los datos leídos
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        z = msg.pose.pose.position.z
        v = msg.twist.twist.linear.x
        a = msg.twist.twist.angular.z
        # imprime los datos leídos       
        self.get_logger().info('Se está recibiendo posicion odom del robot:\n x = {0} \n y = {1}\n z = {2}\n Velocidad lineal= {3}\n Velocidad angular = {4}\n\n '.format(x, y, z, v, a))
        self.get_logger().info('Se está recibiendo "%s"' % str(msg))
        time.sleep(2)

def main(args=None):
    # inicializa la comunicacion ROS2
    rclpy.init(args=args)
    # declara el nodo
    odom_subscriber = Odom_Subscriber()
    # dejamos abierto el nodo hasta ctr+c
    rclpy.spin(odom_subscriber)
    # Destruimos el nodo
    odom_subscriber.destroy_node()
    # se cierra la comunicacion ROS2
    rclpy.shutdown()

if __name__ == '__main__':
    main()
