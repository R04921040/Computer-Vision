import cv2
import numpy as np


lena = cv2.imread('lena.bmp')

height , width , channels = lena.shape


Lena_down_sampling = np.zeros([int(height/8) , int(width/8)])

for i in range(int(height/8)):
    for j in range(int(width/8)):
        if lena[i*8 , j*8  , 0] >= 128:
            Lena_down_sampling[i,j] = 255
        else:
            Lena_down_sampling[i,j] = 0


cv2.imwrite('down_sampling.bmp' , Lena_down_sampling)

# x7 x2 x6
# x3 x0 x1
# x8 x4 x5 

def judge_values(x , y):
    if x >= Lena_down_sampling.shape[0] or x < 0  or y >= Lena_down_sampling.shape[1] or y < 0:
        return 0
    else:
        return Lena_down_sampling[x,y]

def get_neighbors(x,y):
    return [judge_values(x , y) , judge_values(x , y+1) , judge_values(x-1 , y) , 
    judge_values(x , y-1) , judge_values(x+1 , y) , judge_values(x+1 , y+1) ,
    judge_values(x-1 , y+1) , judge_values(x-1 , y-1) , judge_values(x+1 , y-1)]

def def_h(b , c , d , e):
    if b == c and (d != b or e != b):
        return 'q'
    elif b == c and (d == b and e == b):
        return 'r'
    elif b != c:
        return 's'

def def_a(a1 , a2 , a3 , a4):
    four_connected_neighbors = [a1 , a2 , a3 , a4]
    if a1 == a2 == a3 == a4 == 'r':
        return 5
    else :
        return four_connected_neighbors.count('q')

def Yokoi(neighbors):
    return(def_a( def_h(neighbors[0] , neighbors[1] , neighbors[6] , neighbors[2]),
    def_h(neighbors[0] , neighbors[2] , neighbors[7] , neighbors[3]),
    def_h(neighbors[0] , neighbors[3] , neighbors[8] , neighbors[4]),
    def_h(neighbors[0] , neighbors[4] , neighbors[5] , neighbors[1])))

Yokoi_numbers = [[' ' for i in range(Lena_down_sampling.shape[0])] for j in range(Lena_down_sampling.shape[1])]


for i in range(Lena_down_sampling.shape[0]):
    for j in range(Lena_down_sampling.shape[1]):
        if Lena_down_sampling[i,j] !=0:
            neighbors = get_neighbors(i,j)
            Yokoi_numbers[i][j] = Yokoi(neighbors)


output = open('Yoikoi_numbers.txt' , 'w')
for i in range(len(Yokoi_numbers)):
    for j in range(len(Yokoi_numbers[i])):
        output.write(str(Yokoi_numbers[i][j]))
    output.write('\n')
