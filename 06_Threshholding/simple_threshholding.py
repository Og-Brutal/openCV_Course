import os
import cv2


image=cv2.imread(os.path.join("..","Images","image.png"))

image_grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(image_grey, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
thresh=cv2.medianBlur(thresh,7)
cv2.imshow("bear",image_grey)
cv2.imshow("detected_object",thresh)
cv2.waitKey(0)
