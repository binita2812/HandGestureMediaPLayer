import cv2
import numpy as np

# video_reader= cv2.VideoCapture(0)  #reading from webcam

# while True:
#     success, frame=video_reader.read()
#     if not success:
#         break

#     cv2.imshow("My Video", frame)
#     key= cv2.waitKey(10)
#     if key == ord('q'):
#         break

# video_reader.release()
# cv2.destroyAllWindows()

img_path="./images/sherlock_kid.png"
img = cv2.imread(img_path)

img_shape= img.shape
#img_white= np.full(img_shape, 255, dtype=np.uint8)
# img_white=np.array(img)
# img_white[0:150:,::]=255
# print(img_white.shape)
# image_new=img_white - img
# cv2.imshow("new_Image",image_new)
# cv2.waitKey(0)
img_red=np.array(img)
img_red[:,:]=(0,0,50)

img_neww=img + img_red
cv2.imshow("neww Image",img_neww)
cv2.waitKey(0)
