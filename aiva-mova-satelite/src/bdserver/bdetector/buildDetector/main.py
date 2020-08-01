# -*- coding: utf-8 -*-

""" -----------------------------------------------------------------------
Aplicaciones Industriales y Comerciales - Marzo 2019
Grupo segmentación de imágenes satélite - Ignacio Arranz y Carlos Rodríguez
---------------------------- Ignacio Arranz & Carlos Rodríguez-------------

This file contains the main program of the segmentation algorithm of 
Industrial and Commercial Applications subject buildings of the
Official Master in Computer Vision.
"""
from buildDetector import BuildDetector

if __name__== "__main__":

    build_detector = BuildDetector()

    build_detector.buildDetector('./chicago9.tif')

