import rclpy
# importamos las librerias ROS2 de python 
from rclpy.node import Node
# importamos los mensajes tipo Twist
from geometry_msgs.msg import Pose

# creamos una subclase pasándole como parámetro el Nodo 
class GoToPos2(Node):

    def __init__(self):
        # ejecutamos super() inicializa el Nodo
        # introducimos nombre del nodo como parámetro
        super().__init__('pos2_publisher')
        # creamos el objeto publisher
        # la cola del topic es de 100 mensajes
        self.goal_pose_publisher = self.create_publisher(Pose, 'pose', 100)
        self.publish_pos()
    
    def publish_pos(self):
        pose = Pose()
        #pose.header.frame_id = 'map'
        #Pos
        pose.position.x = 0.32
        pose.position.y = 1.77
        pose.orientation.w = 1.0
        self.goal_pose_publisher.publish(pose)
        exit(0)
        
        
            
def main(args=None):
    # inicializa la comunicación
    rclpy.init(args=args)
    # declara el constructor del nodo 
    simple_publisher = GoToPos2()
    # dejamos vivo el nodo
    # para parar el programa habrá que matar el node (ctrl+c)
    rclpy.spin(simple_publisher)
    # destruye en nodo
    simple_publisher.destroy_node()
    # se cierra la comunicacion ROS
    rclpy.shutdown()

if __name__ == '__main__':
    main()
