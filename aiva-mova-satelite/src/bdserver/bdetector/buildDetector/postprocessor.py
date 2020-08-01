# -*- coding: utf-8 -*-

import cv2
import numpy as np


class Postprocessor():

    threshold = 0.25
        
    def recompose_image(self, list_binarized_images):

        '''
        Method that recompose the image from 4 pieces to 1
        
        Args:
            list_binarized_images (list of numpy.ndarray): List of binary images to join.
        
         Returns:
            join_image (numpy.ndarray): One image with 1024x1024 pixels.
        '''        

        join_image = np.zeros((1024, 1024))
        width, height = join_image.shape

        test = []
        for image in list_binarized_images:
            image = image[0, :, :, 0]
            test.append(image)
        
        join_image[:int(width/2), :int(height/2)] = test[0]
        join_image[:int(width/2), int(height/2):] = test[1]
        join_image[int(width/2):, :int(height/2)] = test[2]
        join_image[int(width/2):, int(height/2):] = test[3]

        return join_image


    def rescalate_image(self, image):

        '''
        Method that rescalate the image to 100x100 pixels
        
        Args:
            image (numpy.ndarray): Image to rescalate.
        
         Returns:
            rescalate_image (numpy.ndarray):  Rescalated image.
        '''

        rescalate_image = cv2.resize(image, dsize=(1000, 1000), interpolation=cv2.INTER_CUBIC)

        return rescalate_image


    def umbralized(self, final_image):

        '''
        Method that umbralize the image to convert in a binary image.
        
        Args:
            final_image (numpy.ndarray): Image to process.
        
         Returns:
           thresh (numpy.ndarray):  Binary image.
        '''
        
        ret, thresh = cv2.threshold(final_image, self.threshold, 255, 0)
        
        return thresh


    def postprocess_image(self, list_binarized_images):
        
        '''
        Getting the image from the main program and postprocess it to generate an quality output.
        
        Args:
            list_binarized_images (list of numpy.ndarray): List with of images to process.
        
         Returns:
            final_image_threshhold (numpy.ndarray): Postprocess image.
        '''

        final_image = self.recompose_image(list_binarized_images)
        final_image = self.rescalate_image(final_image)
        final_image_threshhold = self.umbralized(final_image)
        
        return final_image_threshhold

