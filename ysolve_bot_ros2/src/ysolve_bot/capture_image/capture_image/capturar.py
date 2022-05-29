from time import sleep
import rclpy
import cv2
import numpy as np
import requests
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from rclpy.node import Node
from rclpy.qos import ReliabilityPolicy, QoSProfile
from PIL import Image as ImagePIL
import tensorflow as tf
from keras.preprocessing import image 
#Load the saved model
import os
import base64
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
model = tf.keras.models.load_model('src/ysolve_bot/capture_image/capture_image/model/rps.h5')
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
        
        frame=cv_image
        #Convert the captured frame into RGB
        im = ImagePIL.fromarray(frame, 'RGB')
        
        #224x224 train model with this image size.
        im = im.resize((224,224))
       
        img_array =  tf.keras.utils.img_to_array(im)
        img_array = np.expand_dims(img_array, axis=0) / 255
        probabilities = model.predict(img_array)[0]
        #predict method on model to predict 'fire' on the image
        prediction = np.argmax(probabilities)
        #if prediction is > 0.7 , which means there is fire in the frame.
        if probabilities[prediction] > 0.8:
            print("FUEGO")
            print("probabilityAcc",probabilities[prediction])
        print("probabilityLossAcc",probabilities)
        # Nos falta que se guarde la imagen cada X tiempo para ser procesada con openCV -> deteccion de bordes y color para ver si hay un incendio
        # Esta linea guarda la imagen obtenida -> cv2.imwrite("image_copy.jpg",img)
        cv2.waitKey(1)   
        sleep(5)
        # MANDAR IMAGEN A LA API
        self.sendtoserver(cv_image,probabilities[prediction])
        
    def sendtoserver(self,frame,fireProbability):
        imencoded = cv2.imencode(".jpg", frame)[1]
        url = 'http://127.0.0.1:8080/ros/image/send/'+str(imencoded)+'/'+str(fireProbability)        
        try:
            r = requests.post(url, '')
        except Exception as e:
            print(e)
        print("image sent successfully") 
    
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
