import numpy as np
import scipy 

from keras.models import *
from keras.layers import Input, concatenate, Conv1D,Conv2D, MaxPooling2D, UpSampling2D, Dropout, Cropping2D
from keras.optimizers import *
from keras.callbacks import ModelCheckpoint, LearningRateScheduler
from keras import backend as keras

from keras.models import load_model
import cv2

import matplotlib.pyplot as plt

def op(X_test,Y_test,size):
  for i in range(0,size):
    a = Y_test[i].copy()
    c = a.flatten().reshape(512,512)
    plt.figure()
    plt.imshow(c);
    plt.colorbar()
    plt.show()
    
    
    c_bar = X_test[i].reshape(512,512)
    plt.figure()
    plt.imshow(c_bar);
    plt.colorbar()
    plt.show()

model = load_model('aerial_model.h5')

im = cv2.imread('./img/mockup1.tif',cv2.IMREAD_GRAYSCALE)
print(im)
gt = cv2.imread('./img/mockup_1_gt.tif',cv2.IMREAD_GRAYSCALE)
w,h = im.shape
im = im[:int(w/2), :int(w/2)]
gt = gt[:int(w/2), :int(w/2)]
cv2.imwrite("gt1.png", gt)
cv2.imwrite("im1.png", im)
#im = cv2.imread('austin1_1.tif',cv2.IMREAD_GRAYSCALE)

resized_image = cv2.resize(im, (512, 512)) 

#cv2.imshow('image',resized_image)
#cv2.waitKey(1000)

#resized_image = imageio.imread('austin1_1.tif')
X_test = np.expand_dims(resized_image,axis=0)

print(X_test.shape)
X_test = X_test.reshape(*X_test.shape,1)
print(X_test.shape)
X_test = X_test.astype('float32')
X_test/= 255

Y_test = model.predict(X_test, verbose=1)
Y_test[Y_test > 0.25] = 1
Y_test[Y_test <= 0.25] = 0
op(X_test,Y_test,1)
