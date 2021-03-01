import numpy as np
import matplotlib.pyplot as plt
import sys
import cv2




img = cv2.imread('/Lec3/car.jpg',0)
"""plt.imshow(img2,cmap = 'img')
plt.show()"""

gen = cv2.Laplacian(img, cv2.CV_8U)

gen = np.abs(gen)

plt.imshow(gen,cmap='img')
plt.show()

