from time import sleep
import rclpy
import cv2
import numpy as np
import asyncio
import aiohttp
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from rclpy.node import Node
from rclpy.qos import ReliabilityPolicy, QoSProfile

class Ros2OpenCVImageConverter(Node):   

    def __init__(self):

        super().__init__('Ros2OpenCVImageConverter')
        
        self.bridge_object = CvBridge()
        #self.image_sub = self.create_subscription(Image,'/camera/image_raw',self.camera_callback,QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT))
        self.image_sub = self.create_subscription(Image,'/image',self.camera_callback,QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT))
    def camera_callback(self,data):

        try:
            # Seleccionamos bgr8 porque es la codificacion de OpenCV por defecto
            cv_image = self.bridge_object.imgmsg_to_cv2(data, desired_encoding="bgr8")
        except CvBridgeError as e:
            print(e)

        cv2.imshow("Imagen capturada por el robot", cv_image)
        # MANDAR IMAGEN A LA API
        print("response send image to api", self.sendtoserver(cv_image))
        # Nos falta que se guarde la imagen cada X tiempo para ser procesada con openCV -> deteccion de bordes y color para ver si hay un incendio
        # Esta linea guarda la imagen obtenida -> cv2.imwrite("image_copy.jpg",img)
        cv2.waitKey(1)    
        sleep(5)

    async def sendtoserver(self,frame):
        imencoded = cv2.imencode(".jpg", frame)[1]
        url = 'http://192.168.0.119:8080/ros/image/send'
        myobj = {'imagen': imencoded}
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=myobj) as response:
                print(await response.json())
        ''' print("body",myobj)
        try:
            r = requests.post(url, 'working')
        except Exception as e:
            print(e)
        print("image sent successfully") '''
    
def main(args=None):

    rclpy.init(args=args)    
    img_converter_object = Ros2OpenCVImageConverter()    
    
    try:
        rclpy.spin(img_converter_object)
    except KeyboardInterrupt:
        img_converter_object.destroy_node()
        print("Fin del programa!")
    
    cv2.destroyAllWindows() 
        

if __name__ == '__main__':
    main()
