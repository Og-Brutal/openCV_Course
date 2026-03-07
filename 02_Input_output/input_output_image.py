import cv2
import os
#inputting image 
image_path=os.path.join("..","Lesson_01","image.png")
image=cv2.imread(image_path)

#outputing image
# image=cv2.imwrite(os.path.join("..","Images","image_02_output.jpg"),image)

cv2.imshow("frame",image)
cv2.waitKey(0)