import cv2

img_path="./images/sherlock_kid.png"
img = cv2.imread(img_path)
img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV_FULL)
# print(img)
#  print(img.shape)
# cv2.imshow("Image",img)
# cv2.imshow("Gray Image",img_gray)
# cv2.imshow("HSV Image",img_hsv)
# cv2.waitKey(0)

# cv2.imwrite("./images/sherlock_kid_gray.png",img_gray)
img_resized= cv2.resize(img,(500,500))

#print(img.shape)
print(img_gray.shape)
h,w,c=img.shape
img_crop=img_resized[0:,w//2:]
cv2.imshow("Image",img_crop)
cv2.waitKey(0)