import numpy as np
import matplotlib.pyplot as plt
import sys
import cv2



"""1"""

img = cv2.imread('1.jpg',0)
"""plt.imshow(img2,cmap = 'img')
plt.show()"""


"""2"""
gen = cv2.Laplacian(img, cv2.CV_8U)





"""3"""
gen = cv2.bitwise_not(gen)
img = gen


"""4"""
blur = cv2.blur(gen,(21,1))


"""5"""
ret, dst = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)



"""6""" 
kernel = np.ones((1,15),dtype = np.uint8)

dst = cv2.morphologyEx(dst,cv2.MORPH_OPEN,kernel)



"""7"""

contours, hier = cv2.findContours(dst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

"""8"""

boxRegions = []
hsum = 0

for cnt in boxRegions:
	x,y,w,h = cv2.boundingRect(cnt)
	hsum += h
	boxRegions.append((x,y,w,h))

meanHeight = hsum / float(len(contours))

print(meanHeight)
