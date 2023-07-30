import cv2
import numpy as np
img_path='Images/gray_scale.png'
img1=cv2.imread(img_path)
img=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
# cv2.imshow("img",img)


# _,thresh_img=cv2.threshold(gray_scale_img,127,255,cv2.THRESH_BINARY)
# cv2.imshow("img",thresh_img)
# cv2.waitKey(0)
(h,w)=img.shape

for i in range(0,h):
    for j in range(0,w):
        if(img[i,j])>100:
            img[i,j]=255
        else:    
            img[i,j]=0
cv2.imshow("img",img)
cv2.waitKey(0)        
# img_shape= img.shape
# print(img.shape)


