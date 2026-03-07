import os
import cv2

image = cv2.imread(os.path.join("..","Images","paper.png"))

image_grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

thresh=cv2.adaptiveThreshold(image_grey,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,30)
# thresh=cv2.medianBlur(thresh,7)
cv2.imshow("paper",image_grey)
cv2.imshow("thresh",thresh)
cv2.waitKey(0)