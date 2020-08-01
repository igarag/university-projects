# -*- coding: utf-8 -*-

import unittest
import cv2
import numpy as np

from src.preprocessor import Preprocessor
from src.network import Network
from keras.models import load_model
from src.postprocessor import Postprocessor
from src.analitics import Analitics


class Satelitest(unittest.TestCase):
    

    ### PREPROCESSOR
    def test_color2bw(self):
        
        '''
        Loads the main input image to convert it to scale of gray.
        '''
        img_test = cv2.imread('test/img/img.tif')
        dimensions = Preprocessor.color2bw(self, img_test)
        self.assertEqual(np.shape(dimensions), (5000, 5000))


    def test_crop_image(self):

        '''
        Load an image from the test image library into 
        grey scale and pass it to the crop_image function
        which returns an array composed of 4 images of (2500, 2500).

        The test checks the result by validating the dimensions and finally
        that the array is composed of 4 images.
        '''

        img_test = cv2.imread('test/img/test_color_gray.png', cv2.IMREAD_GRAYSCALE)
        cropped = Preprocessor.crop_image(self, img_test)

        self.assertEqual(np.shape(cropped[0]), (2500, 2500))
        self.assertEqual(np.shape(cropped[1]), (2500, 2500))
        self.assertEqual(np.shape(cropped[2]), (2500, 2500))
        self.assertEqual(np.shape(cropped[3]), (2500, 2500))

        self.assertEqual(len(cropped), 4)


    def test_scale_images(self):

        '''
        Loads the 4 pieces of the total image and with dimensions (2500, 2500),
        eliminates one dimension because imread loads with 3 dimensions even if it is
        in grayscale.
        '''

        # Tiene que leer las 4 imágenes que entran
        img_test_1 = cv2.imread('test/img/test_crop_image_1.png', cv2.IMREAD_GRAYSCALE)
        img_test_2 = cv2.imread('test/img/test_crop_image_2.png', cv2.IMREAD_GRAYSCALE)
        img_test_3 = cv2.imread('test/img/test_crop_image_3.png', cv2.IMREAD_GRAYSCALE)
        img_test_4 = cv2.imread('test/img/test_crop_image_4.png', cv2.IMREAD_GRAYSCALE)
    
        img_test_list = [img_test_1, img_test_2, img_test_3, img_test_4]

        scaled = Preprocessor.scale_images(self, img_test_list)

        self.assertEqual(len(scaled), 4)
        self.assertEqual(np.shape(scaled[0]), (512, 512))
        self.assertEqual(np.shape(scaled[1]), (512, 512))
        self.assertEqual(np.shape(scaled[2]), (512, 512))
        self.assertEqual(np.shape(scaled[3]), (512, 512))


    ### NETWORK
    def test_network(self):

        '''
        Load in the neural network the 4 images of the previous stage of
        sequential way, giving the output 4 images with shape (1, 512, 512, 1)
        '''
        model = Network('./docs/aerial_model.h5')

        img_test_1 = cv2.imread('test/img/test_scale_image_1.png', cv2.IMREAD_GRAYSCALE)
        img_test_2 = cv2.imread('test/img/test_scale_image_2.png', cv2.IMREAD_GRAYSCALE)
        img_test_3 = cv2.imread('test/img/test_scale_image_3.png', cv2.IMREAD_GRAYSCALE)
        img_test_4 = cv2.imread('test/img/test_scale_image_4.png', cv2.IMREAD_GRAYSCALE)

        img_test_list = [img_test_1, img_test_2, img_test_3, img_test_4]

        test_output_network = []
        for idx, item in enumerate(img_test_list):
            X_test, Y_test = model.predict(img_test_list[idx])
            test_output_network.append(Y_test)

        self.assertEqual(np.shape(test_output_network[0]), (1, 512, 512, 1))
        self.assertEqual(np.shape(test_output_network[1]), (1, 512, 512, 1))
        self.assertEqual(np.shape(test_output_network[2]), (1, 512, 512, 1))
        self.assertEqual(np.shape(test_output_network[3]), (1, 512, 512, 1))


    ### POSTPROCESS
    def test_recompose_image(self):

        '''
        Upload 4 images that will be the ones that, together, form the final image of (1000, 1000).
        It is necessary to expand the dimension to adapt it to what the network returns.
        neuronal. The numpy function expand_dims is used for it.
        '''

        img_test_1 = cv2.imread('test/img/test_network_1.png', cv2.IMREAD_GRAYSCALE)
        img_test_2 = cv2.imread('test/img/test_network_2.png', cv2.IMREAD_GRAYSCALE)
        img_test_3 = cv2.imread('test/img/test_network_3.png', cv2.IMREAD_GRAYSCALE)
        img_test_4 = cv2.imread('test/img/test_network_4.png', cv2.IMREAD_GRAYSCALE)

        img_test_1 = np.expand_dims(img_test_1, axis=0)
        img_test_1 = np.expand_dims(img_test_1, axis=1)
        img_test_2 = np.expand_dims(img_test_2, axis=0)
        img_test_2 = np.expand_dims(img_test_2, axis=1)
        img_test_3 = np.expand_dims(img_test_3, axis=0)
        img_test_3 = np.expand_dims(img_test_3, axis=1)
        img_test_4 = np.expand_dims(img_test_4, axis=0)
        img_test_4 = np.expand_dims(img_test_4, axis=1)

        img_test_list = [img_test_1, img_test_2, img_test_3, img_test_4]

        recompose = Postprocessor.recompose_image(self, img_test_list)

        self.assertEqual(np.shape(recompose), (1024, 1024))


    def test_umbralized(self):
    
        '''
        Loads the recomposed image (1000, 1000) of the neural network output
        and thresholds the result.
        '''

        img_test = cv2.imread('test/img/test_recompose_image.png', cv2.IMREAD_GRAYSCALE)

        postprocessor = Postprocessor()

        thresh = postprocessor.umbralized(img_test)

        self.assertEqual(np.shape(thresh), (1000, 1000))


    ### ANALYSIS
    def test_analyzer(self):

        '''
        Given a test image returns the values corresponding to the image postprocessor. 
        Values as, areas, central points and areas.
        '''
        
        img_test = cv2.imread('test/img/img.tif')
        img_output_network = cv2.imread('test/img/test_umbralized.png', cv2.IMREAD_GRAYSCALE)

        analizor = Analitics()

        thresh_img, data = analizor.analyze(img_test, img_output_network)

        self.assertEqual(len(data), 1288)


    ### GLOBAL TEST
    # def test_global(self):

    #     '''
    #     Performs a complete test of the algorithm. Given as input, an image offers the output 
    #     image and a fixed.
    #     '''
        
    #     path_img_test = 'test/img/img.tif'
    #     img_output_network = BuildDetector.buildDetector(self, path_img_test)

        


if __name__ == "__main__":
    
    unittest.main()