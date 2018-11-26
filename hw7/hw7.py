import cv2
import numpy as np


lena = cv2.imread('lena.bmp')

height , width , channels = lena.shape

binarize = np.zeros([height,width])

for i in range(height):
    for j in range(width):
        if lena[i , j , 0] >= 128:
            binarize[i , j] = 255

#cv2.imwrite('binarize.bmp' , binarize)
#current_image = binarize

def get_pixel(image,x , y):
    if x < 0 or x >= height or y < 0 or y >= width:
        return 0
    
    return image[x , y]

#  3X3
#  x8 | x1 | x2
#  x7 | x0 | x3
#  x6 | x5 | x4

def get_neighbors(image,x,y):
    neighbors = [get_pixel(image,x , y) , get_pixel(image,x-1 , y) , get_pixel(image,x-1 , y+1),
                 get_pixel(image,x , y+1) , get_pixel(image,x+1 , y+1) , get_pixel(image,x+1 , y),
                 get_pixel(image,x+1 , y-1) , get_pixel(image,x , y-1) , get_pixel(image,x-1 , y-1)]
    
    return neighbors

def count_changed(neighbors):
    counter = 0
    state = neighbors[1]
    temp = list(neighbors)
    del temp[0]
    temp.append(temp[0])
    for i in range(len(temp)):
        if i +1< len(temp):
            if temp[i] < temp [i+1] :
                counter +=1
    return counter

def count_not_zero(neighbors):
    
    return np.sum(neighbors)/255 -1

def first_check(neighbors):
    if count_not_zero(neighbors) >= 2 and count_not_zero(neighbors) <= 6:
        if count_changed(neighbors) == 1:
            if neighbors[1]*neighbors[3]*neighbors[5] == 0 and neighbors[3]*neighbors[5]*neighbors[7] == 0:
                return True
    return False

def second_check(neighbors):
    if count_not_zero(neighbors) >= 2 and count_not_zero(neighbors) <= 6:
        if count_changed(neighbors) == 1:
            if neighbors[1]*neighbors[3]*neighbors[7] == 0 and neighbors[1]*neighbors[5]*neighbors[7] == 0:
                return True
    return False


steady = False

counter = 0
while not steady:
    steady = True
    counter +=1 
    remove_first = []
    remove_second = []
    for i in range(height):
        for j in range(width):
            if binarize[i , j] == 255:
                neighbors = get_neighbors(binarize,i , j)
                if first_check(neighbors) :
                    steady = False
                    remove_first.append((i,j))
    for x,y in remove_first:
        binarize[x,y] = 0

    for i in range(height):
        for j in range(width):
            if binarize[i , j] == 255:
                neighbors = get_neighbors(binarize,i , j)
                if second_check(neighbors):
                    steady = False
                    remove_second.append((i,j))
    for x,y in remove_second:
        binarize[x,y] = 0

    print('counter: {0}'.format(counter))
    print('pixels need to been removed: {0}'.format(len(remove_second+remove_second)))


        
    




cv2.imwrite('thinging.bmp' , binarize)
