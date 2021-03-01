import numpy as np
import matplotlib.pyplot as plt
import sys
import cv2

img = cv2.imread('small.png')
##plt.imshow(img)
#plt.show()


imgCar = cv2.imread('car.jpg',0)
#plt.imshow(imgCar)
#plt.show()


carRGB = cv2.cvtColor(imgCar,cv2.COLOR_BGR2RGB)
#plt.imshow(carRGB)
#plt.show()


plt.imshow(carRGB[...,2],cmap='gray')
plt.show()

"""
grayManual = imgCar[...,0] * 0.114 + imgCar[...,1] * 0.587 + imgCar[...,2] * 0.299

#plt.imshow(grayManual,cmap='gray')
#plt.show()

"""
img2 = np.full((500,500),255,dtype = np.uint8)
img2[200:300,200:300] = 0
plt.imshow(img2,cmap = 'gray')
plt.show()
"""



kernel = np.ones((5,5),dtype=np.float64)/25

manual_filter = cv2.filter2D()"""