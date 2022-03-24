import rclpy
# importamos las librerias ROS2 de python 
from rclpy.node import Node
# importamos los mensajes tipo Twist
from geometry_msgs.msg import Twist

# creamos una clase pasándole como parámetro el Nodo
class GoPosition3(Node):

    def __init__(self):
    
        # Constructor de la clase
        # ejecutamos super() para inicializar el Nodo
        # introducimos el nombre del nodo como parámetro
        
        super().__init__('position3_publisher')
        
        # creamos el objeto publisher
        # que publicara en el topic /cmd_vel 
        # la cola del topic es de 100 mensajes
        
        self.publisher_ = self.create_publisher(Twist, 'cmd_position', 100)
        
        # definimos un periodo para publicar periodicamente
        
        timer_period = 0.5
        
        # creamos un timer con dos parametros:
        # - el periodo (0.5 seconds)
        # - la funcion a realizar  (timer_callback)
        
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        # creamos el mensaje tipo Twist
        msg = Twist()
        # define la velocidad lineal en el eje x 
        pose.position.x = -1.4
        # define la velocidad angular en el eje z
        pose.position.y = 1.1
        # define la orientación w
        pose.orientation.w = 1.0 
        # Publicamos el mensaje en el topic
        self.publisher_.publish(msg)
        # Mostramos el mensaje por el terminal
        self.get_logger().info('Publishing: "%s"' % msg)
        exit(0)
            
def main(args=None):
    # inicializa la comunicación
    rclpy.init(args=args)
    # declara el constructor del nodo 
    simple_publisher = GoPosition3()
    # dejamos vivo el nodo
    # para parar el programa habrá que matar el node (ctrl+c)
    rclpy.spin(simple_publisher)
    # destruye en nodo
    simple_publisher.destroy_node()
    # se cierra la comunicacion ROS
    rclpy.shutdown()

if __name__ == '__main__':
    main()
