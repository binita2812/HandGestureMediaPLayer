import cv2
import numpy as np
img_path='Images/book_page.jpg'
img1=cv2.imread(img_path)
img=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
img2=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
(h,w)=img.shape

for i in range(0,h):
    for j in range(0,w):
        if(img[i,j])>100:
            img[i,j]=255
        else:    
            img[i,j]=0
thresh_val,thresh_image=cv2.threshold(img2,200,255,cv2.THRESH_OTSU)            
cv2.imshow("img",img)
cv2.imshow("img2", thresh_image)
cv2.waitKey(0)   