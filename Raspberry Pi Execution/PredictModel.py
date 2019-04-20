from keras.models import load_model, Sequential
import cv2
import numpy as np


def predicted(image, model):
    model = load_model(model)
    test_image = cv2.imread(image)
    test_image = np.resize(test_image, (1, 128, 128, 3))
    test_image = test_image.astype('float32')
    test_image /= 255.0
    temp = model.predict(test_image)
    return temp


