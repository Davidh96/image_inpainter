import numpy as np
import cv2
from matplotlib import pyplot as plt

#contains functions for processing the image
class imageProcessor():

    #removes any noise from the image, resulting in the structure image
    def structureImage(self):
        img = cv2.imread('TestImages/test.jpg')

        dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

        plt.subplot(121),plt.imshow(img)
        plt.subplot(122),plt.imshow(dst)
        plt.show()

        # img = cv2.imread('messi_2.jpg')


        mask = cv2.imread('TestImages/mask.bmp',0)
        dst = cv2.inpaint(dst,mask,3,cv2.INPAINT_NS)
        cv2.imshow('dst',dst)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


        return dst;

    def textureImage(self):

        denoised=self.structureImage()
        #grey = cv2.cvtColor(denoised, cv2.COLOR_BGR2GRAY)

        # img = cv2.imread('TestImages/test.jpg',-1)
        # RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # completed=RGB_img-grey
        # test=completed+grey
        # plt.subplot(121),plt.imshow(completed)
        # plt.subplot(122),plt.imshow(denoised)
        # plt.subplot(131),plt.imshow(test)
        # plt.show()
