import cv2
import os

image =cv2.imread(os.path.join("..","Images","image_02.jpg"))

print("Original Shape",image.shape)

# Recising

resized_img=cv2.resize(image,(1500,960))

# cropping
# [240:700,400:1400] before comma is the number of rows and and after comma number of columns
cropped_img=resized_img[240:700,400:1400]
cv2.imshow("recized image",resized_img)
cv2.imshow("cropped image",cropped_img)
cv2.waitKey(0)


