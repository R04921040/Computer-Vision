import cv2
import numpy as np
import math

lena = cv2.imread('lena.bmp')
lena = lena[:,:,0]

height , width = lena.shape

def Laplace(image , threshold):
    Laplace1 = np.zeros([height , width])
    Laplace2 = np.zeros([height , width])
    mask1 = np.array([
        [0 , 1 , 0] , [1 , -4 , 1] , [0 , 1 , 0]
    ])

    mask2 = np.array([
        [1 , 1 , 1] , [1 , -8 , 1] , [1 , 1 , 1]
    ])

    for i in range(1 , height-1):
        for j in range(1 , width-1):
            cover = image[i-1:i+2 , j-1:j+2]
            gradient1 = np.sum(cover * mask1)
            gradient2 = np.sum(cover * mask2)/3

            if gradient1 < threshold:
                Laplace1[i , j] = 255
            
            if gradient2 < threshold:
                Laplace2[i , j] = 255
    
    return Laplace1,Laplace2

def min_var_Laplacian(image , threshold):
    min_var_Laplacian = np.zeros([height , width])
    mask = np.array([
        [2 , -1 , 2] , [-1 , -4 , -1] , [2 , -1 , 2]
    ])

    for i in range(1 , height-1):
        for j in range(1 , width-1):
            cover = image[i-1:i+2 , j-1:j+2]
            gradient = np.sum(cover * mask)/3

            if gradient < threshold:
                min_var_Laplacian[i , j] = 255
    
    return min_var_Laplacian

def Laplace_Gaussian(image , threshold):
    Laplace_Gaussian = np.zeros([height , width])
    mask = np.array([
		[0, 0, 0, -1, -1, -2, -1, -1, 0, 0, 0],
		[0, 0, -2, -4, -8, -9, -8, -4, -2, 0, 0],
		[0, -2, -7, -15, -22, -23, -22, -15, -7, -2, 0],
		[-1, -4, -15, -24, -14, -1, -14, -24, -15, -4, -1],
		[-1, -8, -22, -14, 52, 103, 52, -14, -22, -8, -1],
		[-2, -9, -23, -1, 103, 178, 103, -1, -23, -9, -2],
		[-1, -8, -22, -14, 52, 103, 52, -14, -22, -8, -1],
		[-1, -4, -15, -24, -14, -1, -14, -24, -15, -4, -1],
		[0, -2, -7, -15, -22, -23, -22, -15, -7, -2, 0],
		[0, 0, -2, -4, -8, -9, -8, -4, -2, 0, 0],
		[0, 0, 0, -1, -1, -2, -1, -1, 0, 0, 0]
	])

    for i in range(5 , height-5):
        for j in range(5 , width-5):
            cover = image[i-5:i+6 , j-5:j+6]
            gradient = np.sum(cover * mask)

            if gradient < threshold:
                Laplace_Gaussian[i , j] = 255
    
    return Laplace_Gaussian

def diff_Gaussian(image , threshold):
    diff_Gaussian = np.zeros([height , width])
    mask = np.array([
		[-1, -3, -4, -6, -7, -8, -7, -6, -4, -3, -1],
		[-3, -5, -8, -11, -13, -13, -13, -11, -8, -5, -3],
		[-4, -8, -12, -16, -17, -17, -17, -16, -12, -8, -4],
		[-6, -11, -16, -16, 0, 15, 0, -16, -16, -11, -6],
		[-7, -13, -17, 0, 85, 160, 85, 0, -17, -13, -7],
		[-8, -13, -17, 15, 160, 283, 160, 15, -17, -13, -8],
		[-7, -13, -17, 0, 85, 160, 85, 0, -17, -13, -7],
		[-6, -11, -16, -16, 0, 15, 0, -16, -16, -11, -6],
		[-4, -8, -12, -16, -17, -17, -17, -16, -12, -8, -4],
		[-3, -5, -8, -11, -13, -13, -13, -11, -8, -5, -3],
		[-1, -3, -4, -6, -7, -8, -7, -6, -4, -3, -1]
	])

    for i in range(5 , height-5):
        for j in range(5 , width-5):
            cover = image[i-5:i+6 , j-5:j+6]
            gradient = np.sum(cover * mask)
            #print(gradient)
            if gradient > threshold:
                diff_Gaussian[i , j] = 255
    
    return diff_Gaussian

#Laplace1 , Laplace2 = Laplace(lena , 15)
#min_var_Laplacian = min_var_Laplacian(lena , 20)
#Laplace_Gaussian = Gaussian(lena , 3000)
diff_Gaussian = diff_Gaussian(lena , 1)

#cv2.imwrite('Laplacian type1.bmp' , Laplace1)
#cv2.imwrite('Laplacian type2.bmp' , Laplace2)
#cv2.imwrite('min_var_Laplacian.bmp' , min_var_Laplacian)
#cv2.imwrite('Laplace_Gaussian.bmp' , Laplace_Gaussian)
cv2.imwrite('diff_Gaussian.bmp' , diff_Gaussian)