# Nombre: initial_pose.py
# Autor: Ysolve
# Descripción: Script con la lógica necesaria para establecer la posición inicial del robot

# initial_pose_pub.py
import sys
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped

class Publisher(Node):

    '''
    Nodo que publica en el topic /initialpose la posicion a la que se debe dirigir el robot

    Atributes:
        self.publisher_: Publicador
        self.timer_: Timer de callback
    '''

    def __init__(self):
        super().__init__('initial_pose_node')
        self.publisher_ = self.create_publisher(PoseWithCovarianceStamped, 'initialpose', 1)
        timer_period = 1  # seconds
        self.i = 0.0
        self.timer_ = self.create_timer(timer_period, self.callback)

    def callback(self):
        '''
        Callback que ejecuta la acción de publicar en un punto del mapa

        '''

        msg = PoseWithCovarianceStamped()
        msg.header.frame_id = 'map'
        msg.pose.pose.position.x = 0.0
        msg.pose.pose.position.y = -0.1
        msg.pose.pose.orientation.w = 1.0
        
        self.get_logger().info('Publishing  Initial Position  \n X= 0.0 \n Y=-0.1 \n W = 1.0 ')
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    publisher = Publisher()
    try:
        rclpy.spin_once(publisher)
    except KeyboardInterrupt:
        publisher.destroy_node()
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()
