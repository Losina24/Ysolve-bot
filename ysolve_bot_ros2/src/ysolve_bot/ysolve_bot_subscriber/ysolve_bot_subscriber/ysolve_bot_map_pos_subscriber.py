import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped
from rclpy.qos import ReliabilityPolicy, QoSProfile
import time

class Map_pos_subscriber(Node):

    '''
    Nodo que crea una subscripcion al topic /amcl_pose
    Atributes:
        self.subscriber_pos_map: Manejador del subscriptor
    '''

    def __init__(self):
        
        super().__init__('ysolve_bot_map_pos_subscriber')
    
        self.subscriber_pos_map = self.create_subscription(
            PoseWithCovarianceStamped,
            '/amcl_pose',
            self.pose_stamped_callback,
            QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT)
        )    
        self.subscriber_pos_map       

    
    def pose_stamped_callback(self, msg):
        '''
        Callback que es llamado cuando se recibe un mensaje del topic /amcl_pose con la posición
        '''      
        x = msg.position.x
        y = msg.position.y
        z = msg.orientation.z
        w = msg.orientation.w
        # imprime los datos leídos       
        self.get_logger().info('Se está recibiendo posicion sobre el mapa:\n x = {0} \n y = {1}\n Orientación z = {2}\n Orientacion w = {3}\n\n'.format(x, y, z, w))
        time.sleep(2)



def main(args=None):
    # inicializa la comunicacion ROS2
    rclpy.init(args=args)
    # declara el nodo
    map_pos_subscriber= Map_pos_subscriber()
    # dejamos abierto el nodo hasta ctr+c
    rclpy.spin(map_pos_subscriber)
    # Destruimos el nodo
    map_pos_subscriber.destroy_node()
    # se cierra la comunicacion ROS2
    rclpy.shutdown()

if __name__ == '__main__':
    main()
