import numpy as np
import cv2
import matplotlib.pyplot as plt 

lena = cv2.imread('lena.bmp')

#print(lena)
#print(lena.shape)

height , width , channels = lena.shape

histogram = np.zeros(256)

T = 128
thresholding = np.zeros([512,512])
for i in range(height):
    for j in range(width):
        if lena[i , j , 0] >= T:
            thresholding[i , j] = 255

        histogram[lena[i , j , 0]] += 1


####### connected componment 

labels = np.zeros([height , width])
label = 1
eq_set = []

### first pass
for i in range(height):
    for j in range(width):
        
        if j == 0 and i == 0:
            if thresholding[i , j] != 0:
                labels[i , j] = label
                label = label+1
                
        
        elif j == 0 and i != 0:
            if thresholding[i , j] != 0:
                if labels[i-1 , j] != 0:
                    labels[i , j] = labels[i-1 , j]
                else:
                    labels[i , j] = label
                    label = label+1

        elif j != 0 and i == 0:
            if thresholding[i , j] != 0:
                if labels[i , j-1] != 0:
                    labels[i , j] = labels[i , j-1]
                else:
                    labels[i , j] = label
                    label = label+1
        
        else:
            if thresholding[i , j] != 0:
                L = labels[i , j-1]
                U = labels[i-1 , j]
                if L == 0 and U == 0:
                    labels[i , j] = label
                    label = label+1
                
                elif L == 0 and U != 0:
                    labels[i , j] = U
                elif L != 0 and U == 0:
                    labels[i , j] = L
                
                else:
                    labels[i , j] = np.min([U,L])
                    if U != L:
                        if [np.min([U,L]) , np.max([U,L])] not in eq_set:
                            eq_set.append([np.min([U,L]) , np.max([U,L])])

merging = []                    
def merge_set():
    for set in eq_set:

        flag_A = -1
        flag_B = -1
        for i in range(len(merging)):
            if set[0] in merging[i]:
                flag_A = i
            if set[1] in merging[i]:
                flag_B = i

        if flag_A == flag_B and flag_A == -1:
            merging.append(set)
        elif flag_A == -1:
            merging[flag_B].append(set[0])
        elif flag_B == -1:
            merging[flag_A].append(set[1])
        
        else:
            merging[flag_A] = merging[flag_A] + merging[flag_B]
            del merging[flag_B]
merge_set()

for i in range(height):
    for j in range(width):
        L = labels[i , j]
        for k in range(len(merging)):
            if L in merging[k]:
                labels[i , j] = np.min(merging[k])

print(merging)
print(len(merging))
#print(label)

"""
counter = 0
for i in range(height):
    for j in range(width):
        if labels[i,j] is not 1:
            counter = counter +1
print(counter)
"""

#cv2.imwrite('thresholding.bmp', thresholding)
#plt.bar(range(256) , histogram , 1)
#plt.show()