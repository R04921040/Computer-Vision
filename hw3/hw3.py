import cv2
import numpy as np
import matplotlib.pyplot as plt 


lena = cv2.imread('lena.bmp')

#cv2.imshow('lena', lena)
#cv2.waitKey(0)
#cv2.destroyWindow('lena')

height , width , channels = lena.shape
total_pixel = 512*512
histogram = np.zeros(256)

for i in range(height):
    for j in range(width):
        bright = lena[i , j , 0]
        histogram[bright] += 1

Sk = np.zeros(256)
nj = np.zeros(256)
Sk[0] = 255*histogram[0]/total_pixel
nj[0] = histogram[0]
for i in range(1,256):
    nj[i] = nj[i-1] + histogram[i]
    Sk[i]= int(255*nj[i]/total_pixel)

equalization = np.zeros([height , width , channels])
for i in range(height):
    for j in range(width):
        bright = Sk[lena[i , j , 0]]
        equalization[i , j] = [bright , bright , bright]

histogram_equalization = np.zeros(256)

for i in range(height):
    for j in range(width):
        bright = int(equalization[i , j , 0])
        histogram_equalization[bright] += 1

plt.bar(range(256) , histogram_equalization , 1)
plt.show()

"""
cv2.imshow('equalization', equalization)
cv2.waitKey(0)
cv2.destroyWindow('equalization')
"""
cv2.imwrite('equalization.bmp' , equalization)