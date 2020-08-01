# -*- coding: utf-8 -*-
import cv2
import numpy as np
import time

class Preprocessor:

    ''' Class with all necesary functions to preprocess image for network input. '''

    def scale_images(self, list_images):

        '''
        Method that scale list of images to 512x512 pixels.
        
        Args:
            list_images (list of numpy.ndarray): List with images to resize.
        
        Returns:
            resize_images (list of numpy.ndarray): List with resized images.
        '''

        resize_images = [] 
        for img in list_images:
            img = cv2.resize(img, (512, 512)) 
            resize_images.append(img)


        return resize_images 


    def color2bw(self, img):
        
        '''
        Method to convert image from color to black and white
        
        Args:
            img (numpy.ndarray): Image to convert.

        Returns:
            im_bw (numpy.ndarray): Black and white image.
    
        '''

        im_bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        print(im_bw.shape)
        return im_bw


    def crop_image(self, img):

        '''
        Method that crop a image in four equal parts.

        Args:
            img (numpy.ndarray): Image to crop.
        
         Returns:
            images (list of numpy.ndarray): List with four parts of cropped image.
        '''

        width, height = img.shape
        
        images = []
        a = img[:int(width/2), :int(height/2)]
        b = img[:int(width/2), int(height/2):]
        c = img[int(width/2):, :int(height/2)]
        d = img[int(width/2):, int(height/2):]

        images = [a, b, c, d]

        return images


    def preprocess_image(self, img):
        
        '''
        Method that converts a color image to black and white, divides it into four parts, and resizes it to 512x512 pixels.
        
        Args:
            img (numpy.ndarray): Image to process.
        
         Returns:
            images (list of numpy.ndarray):  List of preprocessed images.
        '''

        image = self.color2bw(img)
        images = self.crop_image(image)
        images = self.scale_images(images)

        return images