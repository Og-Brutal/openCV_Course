import cv2
import os

# image read by cv2.imread is always in bgr
image =cv2.imread(os.path.join("..","About_Image","rabbit.png"))

recized_image=cv2.resize(image,(image.shape[1]//2,image.shape[0]//2))
image_rgb=cv2.cvtColor(recized_image,cv2.COLOR_BGR2RGB)
image_GRAY=cv2.cvtColor(recized_image,cv2.COLOR_BGR2GRAY)
image_HSV=cv2.cvtColor(recized_image,cv2.COLOR_BGR2HSV)


cv2.imshow("BGR",recized_image)
cv2.imshow("RGB",image_rgb)
cv2.imshow("Gray",image_GRAY)
cv2.imshow("HSV",image_HSV)
cv2.waitKey(0)