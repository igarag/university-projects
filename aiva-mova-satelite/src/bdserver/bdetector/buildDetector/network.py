# -*- coding: utf-8 -*-

from keras.models import load_model
import numpy as np
import cv2
import matplotlib.pyplot as plt


class Network:

    ''' Core of the application. Contains the neural network that extracts 
    information from the input images.
    '''

    def __init__(self, model_path):
        
        '''
         Constructor of the class. Charge the neural network model from path
        
         Args:
            model_path (string): Path to model file.

         '''

        self.model = load_model(model_path)


    def showResults(self, original_image, segmented_image, size):

        '''
        Method that show the Network output.
        
        Args:
            original_image (numpy.ndarray): Preprocess Image.      

            segmented_image (numpy.ndarray): Segmented Image, output from network.            
            
        '''
        
        for i in range(0,size):
            a = segmented_image[i].copy()
            c = a.flatten().reshape(512,512)
            plt.figure()
            plt.imshow(c);
            plt.colorbar()
            plt.show()

            c_bar = original_image[i].reshape(512,512)
            plt.figure()
            plt.imshow(c_bar);
            plt.colorbar()
            plt.show()


    def predict(self, img):

        '''Takes as input a preprocessed image to calculate the segmented image
        
        Args:
            img (network input): Preprocess image.

        Returns:
            X_test (numpy.ndarray): Preprocess image.

            Y_test (numpy.ndarray): Segmented image.
        '''

        # Change this piece to preprocessor class (expand and reshape)
        X_test = np.expand_dims(img, axis=0)
        X_test = X_test.reshape(*X_test.shape, 1)
        X_test = X_test.astype('float32')
        X_test /= 255
                
        Y_test = self.model.predict(X_test, verbose=1)

        return X_test, Y_test