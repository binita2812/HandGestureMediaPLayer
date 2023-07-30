import cv2
import numpy as np

def nothing(x):
    pass

def createTrackbar():
    cv2.namedWindow("lower1")
    cv2.createTrackbar("L1","lower1", 0, 180, nothing)

    #cv2.namedWindow("lower2")
    cv2.createTrackbar("L2","lower1", 0, 255, nothing)

    #cv2.namedWindow("lower3")
    cv2.createTrackbar("L3","lower1", 0, 255, nothing)
    #cv2.namedWindow("upper1")
    cv2.createTrackbar("U1","lower1", 0, 180, nothing)

    #cv2.namedWindow("upper2")
    cv2.createTrackbar("U2","lower1", 0, 255, nothing)

    #cv2.namedWindow("upper3")
    cv2.createTrackbar("U3","lower1", 0, 255, nothing)

img = cv2.imread('images/hand.jpg')
# cv2.imshow("original image", img)
gray_scale= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray scale image", gray_scale)


# _, thresh_img=cv2.threshold(gray_scale, 127, 255, cv2.THRESH_BINARY)

# cv2.imshow("thresh img", thresh_img)
createTrackbar()

while True:
    L1=cv2.getTrackbarPos("L1","lower1")
    L2=cv2.getTrackbarPos("L2","lower1")
    L3=cv2.getTrackbarPos("L3","lower1")
    U1=cv2.getTrackbarPos("U1","lower1")
    U2=cv2.getTrackbarPos("U2","lower1")
    U3=cv2.getTrackbarPos("U3","lower1")
    # print(T)
    img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower=np.array([L1,L2,L3])
    upper=np.array([U1,U2,U3])
    thresh_img=cv2.inRange(img_hsv,lower,upper)
    cv2.imshow("thresh image", thresh_img)  
    # _,thresh_img=cv2.threshold(gray_scale, T, 255, cv2.THRESH_BINARY)
    # cv2.imshow("threshold", thresh_img)  
    imageCopy=img.copy()

    contours,_=cv2.findContours(thresh_img,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    print(contours)
    cv2.drawContours(imageCopy, contours, -1, (255,0,0), 2)
    cv2.imshow("img", imageCopy)
    key=cv2.waitKey(1)
    if(key==ord('q')):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()