import cv2
import numpy as np


lena = cv2.imread('lena.bmp')

height , width , channels = lena.shape


T = 128
thresholding = np.zeros([512,512])
for i in range(height):
    for j in range(width):
        if lena[i , j , 0] >= T:
            thresholding[i , j] = 255

octogonal_kernel = [
    [0 , 1 , 1 , 1 , 0],
    [1 , 1 , 1 , 1 , 1],
    [1 , 1 , 1 , 1 , 1],
    [1 , 1 , 1 , 1 , 1],
    [0 , 1 , 1 , 1 , 0]
]
#origin at [2,2]

def Dilation(cover):
    for i in range(cover.shape[0]):
        for j in range(cover.shape[1]):
            if octogonal_kernel[i][j] * cover[i][j] == 255:
                return 255

    return 0

def Erosion(cover):
    for i in range(cover.shape[0]):
        for j in range(cover.shape[1]):
            if (octogonal_kernel[i][j] != 0) and (cover[i][j] == 0):
                return 0

    return 255

lena_dilation = np.zeros([height , width])
lena_erosion = np.zeros([height , width])
lena_opening = np.zeros([height , width])
lena_closing = np.zeros([height , width])
for i in range(2 , height-2):
    for j in range(2 , width-2):
        cover = thresholding[i-2:i+3,j-2:j+3]
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

kernel_j = [
    [0 , 0 , 0],
    [1 , 1 , 0],
    [0 , 1 , 0]
]

kernel_k = [
    [0 , 1 , 1],
    [0 , 0 , 1],
    [0 , 0 , 0]
]

#print( thresholding[0][0]==255)


def HitandMiss(image):
    output = np.zeros(image.shape)

    for i in range(1 , image.shape[0] - 1):
        for j in range(1 , image.shape[1] - 1):
            if image[i][j - 1] == 255:
                if image[i][j] == 255:
                    if image[i + 1][j] == 255:
                        if image[i - 1][j] == 0:
                            if image[i - 1][j + 1] == 0:
                                if image[i][j + 1] == 0:
                                    output[i][j] = 255

    cv2.imwrite('HitandMiss.bmp' , output)



HitandMiss(thresholding)
