import cv2,time
import numpy as np
from PIL import Image
import tensorflow as tf
from keras.preprocessing import image
#Load the saved model
key = 0
model = tf.keras.models.load_model('./model/rps.h5')
while True:
        if(key == 0):
                frame = cv2.imread("./image_8.jpg")
        else:
                frame = cv2.imread("./image_0.jpg")
#Convert the captured frame into RGB
        im = Image.fromarray(frame, 'RGB')
#224x224 train model with this image size.
        im = im.resize((224,224))
        img_array = image.img_to_array(im)
        img_array = np.expand_dims(img_array, axis=0) / 255
        probabilities = model.predict(img_array)[0]
        #predict method on model to predict 'fire' on the image
        prediction = np.argmax(probabilities)
        #if prediction is > 0.7 , which means there is fire in the frame.
        if probabilities[prediction] > 0.8:
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                print(probabilities[prediction])
                print("FUEGO")
                print(probabilities[prediction])
        print(probabilities)
        cv2.imshow("Capturing", frame)

        key=cv2.waitKey(3)
        time.sleep(5)
        if key == ord('q'):
                break
        cv2.destroyAllWindows()
        key = 1
