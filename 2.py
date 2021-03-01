import numpy as np
import matplotlib.pyplot as plt
import sys
import cv2


#img = cv2.imread('sudoku.png')
#img = cv2.imread('sudoku.png',0)
"""
plt.imshow(img)
plt.show()
"""


"""
ret,dst = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
plt.imshow(dst, cmap='gray')
plt.show()
"""

"""
dst_adapt = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,
	cv2.THRESH_BINARY,11,2)
plt.imshow(dst_adapt,cmap="gray")
plt.show()
"""

"""
dst_adapt = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
	cv2.THRESH_BINARY_INV,11,2)
	"""
"""
plt.imshow(dst_adapt,cmap="gray")
plt.show()
"""

"""
kernel = np.ones((1,2),dtype = np.uint8)

open = cv2.morphologyEx(dst_adapt,cv2.MORPH_OPEN,kernel,iterations=1)
"""
"""
plt.imshow(open,cmap="gray")
plt.show();
"""

"""
close = cv2.morphologyEx(open,cv2.MORPH_CLOSE,kernel,iterations=1)
plt.imshow(close,cmap="gray")
plt.show();
"""

img = cv2.imread('1.png', 0)



ret, dst = cv2.threshold(img, 70, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

plt.imshow(dst, cmap='gray')
plt.show()


contours, hier = cv2.findContours(dst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

vis = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
img_cnts = cv2.drawContours(vis, contours, -1, (0,255,0), 2)

for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(img_cnts, (x,y), (x+w, y+h), (255,0,0), 1)


plt.imshow(img_cnts)
plt.show()

print(len(contours))