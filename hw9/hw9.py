import cv2
import numpy as np
import math

lena = cv2.imread('lena.bmp')
lena = lena[:,:,0]

height , width = lena.shape

"""
Robert's Operator: 12

Prewitt's Edge Detector: 24

Sobel's Edge Detector: 38

Frei and Chen's Gradient Operator: 30

Kirsch's Compass Operator: 135

Robinson's Compass Operator: 43

Nevatia-Babu 5x5 Operator: 12500
"""

def Robert_operator(image , threshold):
    Robert = np.zeros([height , width])
    mask = np.array([ [[-1 , 0],[0 , 1]] , [[0 , 1],[-1 , 0]] ])
    for i in range(height-1):
        for j in range(width-1):
            cover = image[i:i+2 , j:j+2]
            r1 = np.sum(cover * mask[0])
            r2 = np.sum(cover * mask[1])
            gradient = math.sqrt(math.pow(r1 , 2) + math.pow(r2 , 2))
            if gradient < threshold:
                Robert[i , j] = 255
    
    return Robert

def Prewitt_operator(image , threshold):
    Prewitt = np.zeros([height , width])
    mask = np.array([[[-1 , 0 , 1] , [-1 , 0 , 1] , [-1 , 0 , 1]] , [[-1 , -1 , -1] , [0 , 0 , 0] , [1 , 1 , 1]]])
    for i in range(1 , height-1):
        for j in range(1 , width-1):
            cover = image[i-1:i+2 , j-1:j+2]
            r1 = np.sum(cover * mask[0])
            r2 = np.sum(cover * mask[1])
            gradient = math.sqrt(math.pow(r1 , 2) + math.pow(r2 , 2))
            if gradient < threshold:
                Prewitt[i , j] = 255
    return Prewitt

def Sobel_operator(image , threshold):
    Sobel = np.zeros([height , width])
    mask = np.array([[[-1 , 0 , 1] , [-2 , 0 , 2] , [-1 , 0 , 1]] , [[-1 , -2 , -1] , [0 , 0 , 0] , [1 , 2 , 1]]])
    for i in range(1 , height-1):
        for j in range(1 , width-1):
            cover = image[i-1:i+2 , j-1:j+2]
            s1 = np.sum(cover * mask[0])
            s2 = np.sum(cover * mask[1])
            gradient = math.sqrt(math.pow(s1 , 2) + math.pow(s2 , 2))
            if gradient < threshold:
                Sobel[i , j] = 255
    return Sobel      

def Frei_operator(image , threshold):
    Frei = np.zeros([height , width])
    mask = np.array([[[-1 , 0 , 1] , [-math.sqrt(2) , 0 , math.sqrt(2)] , [-1 , 0 , 1]] , [[-1 , -math.sqrt(2) , -1] , [0 , 0 , 0] , [1 , math.sqrt(2) , 1]]])
    for i in range(1 , height-1):
        for j in range(1 , width-1):
            cover = image[i-1:i+2 , j-1:j+2]
            s1 = np.sum(cover * mask[0])
            s2 = np.sum(cover * mask[1])
            gradient = math.sqrt(math.pow(s1 , 2) + math.pow(s2 , 2))
            if gradient < threshold:
                Frei[i , j] = 255
    return Frei     

def Kirsch_operator(image , threshold):
    Kirsch = np.zeros([height , width])
    mask = np.array([[[-3 , -3 , -3] , [-3 , 0 , -3] , [5 , 5 , 5]],
                     [[-3 , -3 , -3] , [5 , 0 , -3] , [5 , 5 , -3]],
                     [[5 , -3 , -3] , [5 , 0 , -3] , [5 , -3 , -3]],
                     [[5 , 5 , -3] , [5 , 0 , -3] , [-3 , -3 , -3]],
                     [[5 , 5 , 5] , [-3 , 0 , -3] , [-3 , -3 , -3]],
                     [[-3 , 5 , 5] , [-3 , 0 , 5] , [-3 , -3 , -3]],
                     [[-3 , -3 , 5] , [-3 , 0 , 5] , [-3 , -3 , 5]],
                     [[-3 , -3 , -3] , [-3 , 0 , 5] , [-3 , 5 , 5]]])
    for i in range(1 , height-1):
        for j in range(1 , width-1):
            cover = image[i-1:i+2 , j-1:j+2]
            gradient = np.zeros(8)
            for m in range(8):
                gradient = np.sum(cover * mask[m])
            gradient = np.max(gradient)
            if gradient < threshold:
                Kirsch[i , j] = 255
    return Kirsch   

def Robinson_operator(image , threshold):
    Robinson = np.zeros([height , width])
    mask = np.array([[[-1 , -2 , -1] , [0 , 0 , 0] , [1 , 2 , 1]],
                     [[0 , -1 , -2] , [1 , 0 , -1] , [2 , 1 , 0]],
                     [[1 , 0 , -1] , [2 , 0 , -2] , [1 , 0 , -1]],
                     [[2 , 1 , 0] , [1 , 0 , -1] , [0 , -1 , -2]],
                     [[1 , 2 , 1] , [0 , 0 , 0] , [-1 , -2 , -1]],
                     [[0 , 1 , 2] , [-1 , 0 , 1] , [-2 , -1 , 0]],
                     [[-1 , 0 , 1] , [-2 , 0 , 2] , [-1 , 0 , 1]],
                     [[-2 , -1 , 0] , [-1 , 0 , 1] , [0 , 1 , 2]]])
    for i in range(1 , height-1):
        for j in range(1 , width-1):
            cover = image[i-1:i+2 , j-1:j+2]
            gradient = np.zeros(8)
            for m in range(8):
                gradient = np.sum(cover * mask[m])
            gradient = np.max(gradient)
            if gradient < threshold:
                Robinson[i , j] = 255
    return Robinson


def Nevatia_operator(image , threshold):
    Nevatia = np.zeros([height , width])
    mask = np.array([[[100 , 100 , 0 , -100 , -100] , [100 , 100 , 0 , -100 , -100] , [100 , 100 , 0 , -100 , -100] , [100 , 100 , 0 , -100 , -100] , [100 , 100 , 0 , -100 , -100]],
                     [[100 , 100 , 100 , 32 , -100] , [100 , 100 , 92 , -178 , -100] , [100 , 100 , 0 , -100 , -100] , [100 , 78 , -92 , -100 , -100] , [100 , -32 , -100 , -100 , -100]],
                     [[100 , 100 , 100 , 100 , 100] , [100 , 100 , 100 , 78 , -32] , [100 , 92 , 0 , -92 , -100] , [32 , -78 , -100 , -100 , -100] , [-100 , -100 , -100 , -100 , -100]],
                     [[-100 , -100 , -100 , -100 , -100] , [-100 , -100 , -100 , -100 , -100] , [0 , 0 , 0 , -0 , 0] , [100 , 100 , 100 , 100 , 100] , [100 , 100 , 100 , 100 , 100]],
                     [[-100 , -100 , -100 , -100 , -100] , [32 , -78 , -100 , -100 , -100] , [100 , 92 , 0 , -92 , -100] , [100 , 100 , 100 , 78 , -32] , [100 , 100 , 100 , 100 , 100]],
                     [[100 , -32 , -100 , -100 , -100] , [100 , 78 , -92 , -100 , -100] , [100 , 100 , 0 , -100 , -100] , [100 , 100 , 92 , -78 , -100] , [100 , 100 , 100 , 32 , -100]]])
    for i in range(2 , height-2):
        for j in range(2 , width-2):
            cover = image[i-2:i+3 , j-2:j+3]
            gradient = np.zeros(6)
            for m in range(6):
                gradient = np.sum(cover * mask[m])
            gradient = np.max(gradient)
            if gradient < threshold:
                Nevatia[i , j] = 255
    return Nevatia

Robert = Robert_operator(lena , 12)
cv2.imwrite('Robert.bmp' , Robert)

Prewitt = Prewitt_operator(lena , 24)
cv2.imwrite('Prewitt.bmp' , Prewitt)

Sobel = Sobel_operator(lena , 38)
cv2.imwrite('Sobel.bmp' , Sobel)

Frei = Frei_operator(lena , 30)
cv2.imwrite('Frei.bmp' , Frei)

Kirsch = Kirsch_operator(lena , 135)
cv2.imwrite('Kirsch.bmp' , Kirsch)

Robinson = Robinson_operator(lena , 43)
cv2.imwrite('Robinson.bmp' , Robinson)

Nevatia = Nevatia_operator(lena , 12500)
cv2.imwrite('Nevatia.bmp' , Nevatia)
