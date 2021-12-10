import cv2
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import models,utils
import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img,img_to_array
from tensorflow.python.keras import utils
from tensorflow.keras.applications.resnet50 import ResNet50
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.applications.resnet50 import decode_predictions
#from keras.models import load_model
 
model = load_model(r'./resnet_model.h5')
def predict(img_path):

  image = load_img(img_path, target_size=(128, 128))
  img = np.array(image)
  img = img / 255.0
  img = img.reshape(1,128,128,3)
  label = model.predict(img)
  
  result = np.where(label == np.amax(label,axis=1))
  #print("Predicted labels", label[0][0],label[0][1],label[0][2],label[0][3])

  if result[1]==[0]:
    return "Patient is COVID +ve"
  if result[1]==[1]:
    return "Patient is suffering from Lung Opacity"
  if result[1]==[2]:
    return "Patient is Normal"
  if result[1]==[3]:
    return "Patient has Viral Pneumonia"

