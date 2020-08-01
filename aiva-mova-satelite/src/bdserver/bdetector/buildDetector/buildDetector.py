# -*- coding: utf-8 -*-

import cv2
import numpy as np
from os import path
from .preprocessor import Preprocessor
from .postprocessor import Postprocessor
from .network import Network
from .analitics import Analitics

class BuildDetector:

    ''' Main class of proyect, with all necesary process to building detection in satellite images. '''

    def buildDetector(self, img_path):
        
        '''
           Method that charge image from path and detect the buildings

           Args:
            image_path (string): Path to image.
        '''

        resources_dir = path.join(path.dirname(__file__), 'models')

        network = Network(resources_dir + '/aerial_model.h5')
        #network = Network('models/aerial_model.h5')

        img = cv2.imread(img_path)

        ### Preprocessor
        preprocessor = Preprocessor()
        preprocess_images = preprocessor.preprocess_image(img)

        ### Network. Return X and Y test
        output_network = []
        for idx, item in enumerate(preprocess_images):
            X_test, Y_test = network.predict(preprocess_images[idx])
            #network.showResults(X_test, Y_test, 1)
            output_network.append(Y_test)

        ### Postprocess (Y_test ES LA QUE HAY QUE BINARIZAR)
        postprocessor = Postprocessor()
        postprocess_image = postprocessor.postprocess_image(output_network)

        img = postprocessor.rescalate_image(img)
        
        ### Analysis
        analyser = Analitics()
        segmented_image, data = analyser.analyze(img, postprocess_image)
        return segmented_image, data, postprocess_image
        
