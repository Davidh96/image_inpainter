import numpy as np
import cv2
from matplotlib import pyplot as plt

#contains functions for processing the image
class imageProcessor():

    #removes any noise from the image, resulting in the structure image
    def denoiseImage(self):
        img = cv2.imread('TestImages/test.jpg',-1)
        RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        dst = cv2.fastNlMeansDenoisingColored(RGB_img,None,10,10,7,21)

        plt.subplot(121),plt.imshow(RGB_img)
        plt.subplot(122),plt.imshow(dst)
        plt.show()
