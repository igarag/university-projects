# -*- coding: utf-8 -*-

import cv2
import numpy as np
import os
import json


class Analitics:

    '''Extracts information about the output of the neural network to draw conclusions.'''

    def getContours(self, image_thresh):

        '''
        Method that obtains the values of the contours of the segmented image.

        Args:
            image_thresh (numpy.ndarray): Image to process.
        
         Returns:
            array: With all the contours of the buildings.
        '''   

        image_thresh = image_thresh.astype(np.uint8)
        contours, hierarchy = cv2.findContours(image_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        return contours


    def drawBuilding(self, input_image, contours):

        '''
        Method that draws on top of them with a rectangle and the center of this pointing 
        to the coordinate of the building.

        Args:
            input image (numpy.ndarray): Original image.

            contours (array): Contours of the buildings.
        
         Returns:

            img (numpy.ndarray): Image with contours drawed.

            center_houses (array): Center of the buildings (coordenates).
        '''

        img = cv2.resize(input_image, (1000, 1000)) 

        # For each of the contours paint it on the original image
        center_houses = []
        for cnt in contours:
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.drawContours(img, [cnt], 0, (0,255,0), cv2.FILLED)
            cv2.circle(img, (int((x+(w/2))), int((y+(h/2)))),1,(0,255,0),-1)
            center_houses.append((int((x+(w/2))), int((y+(h/2)))))
        
        #cv2.imwrite('./data/output.png', img)

        return img, center_houses


    def exportData(self, image_thresh, building_centers, contours):

        '''
        Method that exports in a file the values of the coordinates, contours and area of buildings.

        Args:
            image_thresh (numpy.ndarray): Threshold image with buildings detection.
            building_centers (array): Center of buildings.
            contours (array): Contours of the buildings.
        
         Returns:
            areas (array): List with bulding areas

        '''

        building_areas = []
        for cnt in contours:
            building_areas.append(cv2.contourArea(cnt))

        buldings_number = len(contours)
        building_area = 100 * (image_thresh == 255).sum() / (image_thresh.shape[0] * image_thresh.shape[1])
        not_building_area = 100 * (image_thresh == 0).sum() / (image_thresh.shape[0] * image_thresh.shape[1])

        data = {
            'buldings_number' : buldings_number,
            'building_area' : building_area,
            'not_building_area' : not_building_area,
            'bulding_centers' : building_centers,
            'buildings_areas' : building_areas
        }

        data = json.dumps(data)

        # Write the results in a file        
        # with open('bdetector/buildDetector/data/data.txt', 'w') as f:
        #     print('Number of houses: ', file=f)
        #     print(str(len(contours)), file=f)
        #     print('\nAreas:', file=f)
        #     print(str(areas), file=f)
        #     print('\nCoords:', file=f)
        #     print(str(center_houses), file=f) 
            
        return data


    def analyze(self, input_image, image_thresh):

        '''
        Main program of this class.

        Args:
            input_image (numpy.ndarray): Original image.
            image_thresh (numpy.ndarray): Threshold image.
        
         Returns:
            segmented_image (numpy.ndarray): Image with contours drawed.
            areas (array): List with bulding areas
        '''

        contours = self.getContours(image_thresh)
        segmented_image, center_houses = self.drawBuilding(input_image, contours)
        data = self.exportData(image_thresh, center_houses, contours)

        return segmented_image, data
