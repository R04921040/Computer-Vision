import cv2
import numpy as np



lena = cv2.imread('lena.bmp')

height , width , channels = lena.shape

binarize = np.zeros([height,width])


def Gaussian_noise(image , amplitude):
    new_image = np.array(image[:,:,0])
    for i in range(height):
        for j in range(width):
            noise = np.random.normal(0 , 1) * amplitude
            if (new_image[i][j] + noise) > 255:
                new_image[i][j] = 255
            elif (new_image[i][j] + noise) < 0:
                new_image[i][j] = 0
            else :
                new_image[i][j] = new_image[i][j]+ noise
    
    return new_image


def Salt_and_Pepper(image , probility):
    new_image = np.array(image[:,:,0])
    for i in range(height):
        for j in range(width):
            rand = np.random.rand()
            if rand < probility:
                new_image[i][j] = 0
            elif rand > 1 - probility:
                new_image[i][j] = 255

    return new_image

Gaussian10 = Gaussian_noise(lena , 10)
Gaussian30 = Gaussian_noise(lena , 30)

SAP005 = Salt_and_Pepper(lena , 0.05)
SAP010 = Salt_and_Pepper(lena , 0.1)


# all weights in box are 1
def box_filter(image , box_height , box_width):
    filted_image = np.array(image)

    for i in range(1 , height-1):
        for j in range(1 , width-1):
            filted_image[i , j] = np.mean(filted_image[i-1:i+2 , j-1:j+2])
    
    return filted_image

def median_filter(image , box_height , box_width):
    filted_image = np.array(image)

    for i in range(int(box_height/2) , height - int(box_height/2)):
        for j in range(int(box_width/2) , width - int(box_width/2)):
            flat = filted_image[i- int(box_height/2) : i + int(box_height/2)+1 , j-int(box_width/2) : j + int(box_width/2)+1].flatten()
            flat.sort()
            filted_image[i , j] = flat[int((box_height*box_width)/2)]

    return filted_image

octogonal_kernel_dilation = [
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

def Dilation(image):
    D = np.array(image)
    for i in range(2 , height-2):
        for j in range(2 , width-2):
            D[i][j] = np.max(octogonal_kernel_dilation * image[i-2:i+3 , j-2:j+3])
    return D

def Erosion(image):
    E = np.array(image)
    for i in range(2 , height-2):
        for j in range(2 , width-2):
            E[i][j] = np.min(octogonal_kernel_erosion * image[i-2:i+3 , j-2:j+3])
    return E

def Opening(image):
    return Dilation(Erosion(image))

def Closing(image):
    return Erosion(Dilation(image))

def Closing_then_Opening(image):
    return Opening(Closing(image))

def Opening_then_Closing(image):
    return Closing(Opening(image))





cv2.imwrite('Gaussian10.bmp' , Gaussian10)
cv2.imwrite('Gaussian30.bmp' , Gaussian30)

cv2.imwrite('SAP005.bmp' , SAP005)
cv2.imwrite('SAP010.bmp' , SAP010)




#Gausian  10
Gaussian10_33box = box_filter(Gaussian10 , 3 , 3)
Gaussian10_55box = box_filter(Gaussian10 , 5 , 5)

Gaussian10_33med = median_filter(Gaussian10 , 3 , 3)
Gaussian10_55med = median_filter(Gaussian10 , 5 , 5)

Gaussian10_closing_then_opening = Closing_then_Opening(Gaussian10)
Gaussian10_openiong_then_closing = Opening_then_Closing(Gaussian10)

cv2.imwrite('Gaussian10_33box.bmp' , Gaussian10_33box)
cv2.imwrite('Gaussian10_55box.bmp' , Gaussian10_55box)
cv2.imwrite('Gaussian10_33med.bmp' , Gaussian10_33med)
cv2.imwrite('Gaussian10_55med.bmp' , Gaussian10_55med)
cv2.imwrite('Gaussian10_closing_then_opening.bmp' , Gaussian10_closing_then_opening)
cv2.imwrite('Gaussian10_openiong_then_closing.bmp' , Gaussian10_openiong_then_closing)

#Gausian  30
Gaussian30_33box = box_filter(Gaussian30 , 3 , 3)
Gaussian30_55box = box_filter(Gaussian30 , 5 , 5)

Gaussian30_33med = median_filter(Gaussian30 , 3 , 3)
Gaussian30_55med = median_filter(Gaussian30 , 5 , 5)

Gaussian30_closing_then_opening = Closing_then_Opening(Gaussian30)
Gaussian30_openiong_then_closing = Opening_then_Closing(Gaussian30)

cv2.imwrite('Gaussian30_33box.bmp' , Gaussian30_33box)
cv2.imwrite('Gaussian30_55box.bmp' , Gaussian30_55box)
cv2.imwrite('Gaussian30_33med.bmp' , Gaussian30_33med)
cv2.imwrite('Gaussian30_55med.bmp' , Gaussian30_55med)
cv2.imwrite('Gaussian30_closing_then_opening.bmp' , Gaussian30_closing_then_opening)
cv2.imwrite('Gaussian30_openiong_then_closing.bmp' , Gaussian30_openiong_then_closing)

#salt and pepper  0.05
SAP005_33box = box_filter(SAP005 , 3 , 3)
SAP005_55box = box_filter(SAP005 , 5 , 5)

SAP005_33med = median_filter(SAP005 , 3 , 3)
SAP005_55med = median_filter(SAP005 , 5 , 5)

SAP005_closing_then_opening = Closing_then_Opening(SAP005)
SAP005_openiong_then_closing = Opening_then_Closing(SAP005)

cv2.imwrite('SAP005_33box.bmp' , SAP005_33box)
cv2.imwrite('SAP005_55box.bmp' , SAP005_55box)
cv2.imwrite('SAP005_55med.bmp' , SAP005_33med)
cv2.imwrite('SAP005_55med.bmp' , SAP005_55med)
cv2.imwrite('SAP005_closing_then_opening.bmp' , SAP005_closing_then_opening)
cv2.imwrite('SAP005_openiong_then_closing.bmp' , SAP005_openiong_then_closing)

#salt and pepper  0.1
SAP010_33box = box_filter(SAP010 , 3 , 3)
SAP010_55box = box_filter(SAP010 , 5 , 5)

SAP010_33med = median_filter(SAP010 , 3 , 3)
SAP010_55med = median_filter(SAP010 , 5 , 5)

SAP010_closing_then_opening = Closing_then_Opening(SAP010)
SAP010_openiong_then_closing = Opening_then_Closing(SAP010)

cv2.imwrite('SAP010_33box.bmp' , SAP010_33box)
cv2.imwrite('SAP010_55box.bmp' , SAP010_55box)
cv2.imwrite('SAP010_33med.bmp' , SAP010_33med)
cv2.imwrite('SAP010_55med.bmp' , SAP010_55med)
cv2.imwrite('SAP010_closing_then_opening.bmp' , SAP010_closing_then_opening)
cv2.imwrite('SAP010_openiong_then_closing.bmp' , SAP010_openiong_then_closing)





