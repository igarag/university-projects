#!/usr/bin/python
# -*- coding: utf-8 -*-

""" -----------------------------------------------------------------------
Aplicaciones Industriales y Comerciales - Marzo 2019
Grupo segmentación de imágenes satélite - Ignacio Arranz y Carlos Rodríguez
---------------------------------------------- Ignacio Arranz -------------

Este código forma parte de un mockup que pone a prueba una de las características
finales del proyecto, segmentar tejados de edificios. Se asume que la red ha 
devuelto la imagen segmentada y se ofrece el paso final, ofrecer al usuario el 
resultado.
"""

__author__  = "Ignacio Arranz"
__license__ = "GPL"
__email__   = "n.arranz.agueda@gmail.com"
__status__  = "Exercise"

import cv2
import numpy


# Choose between two images (for now)
chosen_image = str(input("Choose an option (1 or 2): "))

if int(chosen_image) in range(1,3):
	# Read the image
	path_img = ("./img/img_test_" + chosen_image + ".png")
	img = cv2.imread(path_img)

	# Grayscale image and threshold
	imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	ret,thresh = cv2.threshold(imgray, 127, 255, 0)

	# Search the contours of the segmented image
	contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	# For each of the contours paint it on the original image
	cnt = contours[4]
	for cnt in contours:
		cv2.drawContours(img, [cnt], 0, (0,255,0), 3)
		cv2.imshow("Image " + chosen_image, img)

	# Releasing Resources
	cv2.waitKey(0)
	cv2.destroyAllWindows()
else:
	print("Please, choose between 1 or 2")