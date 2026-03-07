import cv2
import os

webcam=cv2.VideoCapture(0)

while(True):
    re,frame=webcam.read()
    cv2.imwrite(os.path.join("..","About_Image","wahab.png"),frame)
    break

image=cv2.imread(os.path.join("..","About_Image","wahab.png"))
noice_free_image=cv2.medianBlur(image,7)
cv2.imshow("frame",image)
cv2.imshow("noice_free_image",noice_free_image)
cv2.waitKey(0)
