import cv2
import numpy as np


lena = cv2.imread('lena.bmp')

height , width , channels = lena.shape

"""
T = 128
thresholding = np.zeros([512,512])
for i in range(height):
    for j in range(width):
        if lena[i , j , 0] >= T:
            thresholding[i , j] = 255
"""
octogonal_kernel = [
    [0 , 1 , 1 , 1 , 0],
    [1 , 1 , 1 , 1 , 1],
    [1 , 1 , 1 , 1 , 1],
    [1 , 1 , 1 , 1 , 1],
    [0 , 1 , 1 , 1 , 0]
]

octogonal_kernel_erosion = [
    [9999 , 1 , 1 , 1 , 9999],
    [1 , 1 , 1 , 1 , 1],
    [1 , 1 , 1 , 1 , 1],
    [1 , 1 , 1 , 1 , 1],
    [9999 , 1 , 1 , 1 , 9999]
]
#origin at [2,2]

def Dilation(cover):
    return np.max(octogonal_kernel * cover)

def Erosion(cover):
    return np.min(octogonal_kernel_erosion * cover)

lena_dilation = np.zeros([height , width])
lena_erosion = np.zeros([height , width])
lena_opening = np.zeros([height , width])
lena_closing = np.zeros([height , width])
for i in range(2 , height-2):
    for j in range(2 , width-2):
        cover = lena[i-2:i+3,j-2:j+3,0]
        lena_dilation[i][j] = Dilation(cover)
        lena_erosion[i][j] = Erosion(cover)



for i in range(2 , height-2):
    for j in range(2 , width-2):
        cover = lena_dilation[i-2:i+3,j-2:j+3]
        lena_closing[i][j] = Erosion(cover)

        cover = lena_erosion[i-2:i+3,j-2:j+3]
        lena_opening[i][j] = Dilation(cover)


cv2.imwrite('dilation.bmp' , lena_dilation)
cv2.imwrite('erosion.bmp' , lena_erosion)
cv2.imwrite('closing.bmp' , lena_closing)
cv2.imwrite('opening.bmp' , lena_opening)



