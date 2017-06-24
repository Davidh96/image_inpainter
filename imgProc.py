import numpy as np
import cv2
from matplotlib import pyplot as plt
from random import randint
from time import time
from PIL import Image

#contains functions for processing the image
class imageProcessor():

    #removes any noise from the image, resulting in the structure image
    def structureImage(self):
        img = cv2.imread('TestImages/test.jpg',0)

        dst = self.denoiseImage(img)

        mask = cv2.imread('TestImages/mask.bmp',0)
        dst = cv2.inpaint(dst,mask,3,cv2.INPAINT_NS)
        cv2.imshow('original',img)
        cv2.imshow('impainted',dst)

        return dst

    def denoiseImage(self,img):
        return cv2.fastNlMeansDenoising(img,None,10,10,7)

    def textureImage(self):
        img = cv2.imread('TestImages/test.jpg',0)

        edged=self.edgeDetection(img)
        edged = cv2.bitwise_not(edged)

        cv2.imshow('edge',edged)

        mask = cv2.imread('TestImages/mask.bmp',0)
        mask = cv2.bitwise_not(mask)
        texture=mask-edged
        cv2.imshow('texture',texture)

        return texture


    def edgeDetection(self,img):
        edges = cv2.Canny(img,200,300)
        return edges
