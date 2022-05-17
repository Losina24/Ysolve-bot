import rclpy
import cv2
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from rclpy.node import Node
from rclpy.qos import ReliabilityPolicy, QoSProfile

import time
from PIL import Image
import tensorflow as tf
from keras.preprocessing import image

model = tf.keras.models.load_model('./resource/model/rps.h5')

class Ros2OpenCVImageConverter(Node):

    def __init__(self):

        super().__init__('Ros2OpenCVImageConverter')

        self.bridge_object = CvBridge()
        self.image_sub = self.create_subscription(
            Image, '/camera/image_raw', self.camera_callback, QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT))

    def camera_callback(self, data):

        try:
            # Seleccionamos bgr8 porque es la codificacion de OpenCV por defecto
            cv_image = self.bridge_object.imgmsg_to_cv2(
                data, desired_encoding="bgr8")
        except CvBridgeError as e:
            print(e)

        cv2.imshow("Imagen capturada por el robot", cv_image)
        # Nos falta que se guarde la imagen cada X tiempo para ser procesada con openCV -> deteccion de bordes y color para ver si hay un incendio
        # Esta linea guarda la imagen obtenida -> cv2.imwrite("image_copy.jpg",img)
        cv2.waitKey(1)
        time.sleep(2)
# Convert the captured frame into RGB
        im = Image.fromarray(cv_image, 'RGB')
# Resizing into 224x224  we trained the model with this resolution.
        im = im.resize((224, 224))
        img_array = image.img_to_array(im)
        img_array = np.expand_dims(img_array, axis=0) / 255
        probabilities = model.predict(img_array)[0]
        # Prediction of the image
        prediction = np.argmax(probabilities)
        print(prediction)
        # if prediction is 0, which means there is fire in the frame.
        if prediction == 0:
            # Fire Probability
            print(probabilities[prediction])
            print("FUEGO")
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        cv2.destroyAllWindows()


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
