import numpy as np
import cv2

lena = cv2.imread('lena.bmp')

print(type(lena))
print(lena.shape)

# 顯示圖片
#cv2.imshow('lena', lena)

#cv2.imwrite('output.jpg', img)
# 按下任意鍵則關閉所有視窗
#cv2.waitKey(0)
#cv2.destroyWindow('lena')
#cv2.destroyAllWindows()

#512 , 512 , 3
x , y , channels = lena.shape

upside_down = np.zeros(lena.shape)
right_side_left = np.zeros(lena.shape)
diagonally_mirrored = np.zeros(lena.shape)


for i in range(x):
    for j in range(y):
        upside_down[i , j] = lena[x-1 - i , j]
        right_side_left[i , j] = lena[i , y-1 - j]
        diagonally_mirrored[i , j] = lena[x-1 - i , y-1 - j]


#cv2.imshow('upside_down', upside_down)
#cv2.imshow('right_side_left', right_side_left)
#cv2.imshow('diagonally_mirrored', diagonally_mirrored)

#cv2.waitKey(0)
#cv2.destroyAllWindows()

cv2.imwrite('upside_down.jpg', upside_down)
cv2.imwrite('right_side_left.jpg', right_side_left)
cv2.imwrite('diagonally_mirrored.jpg', diagonally_mirrored)