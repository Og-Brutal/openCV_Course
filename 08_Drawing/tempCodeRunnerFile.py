import cv2
import os 


image =cv2.imread(os.path.join("..","Images","white_board.png"))
print(image.shape)
# Line
# cv2.line(image,(x,y),(x,y),(color),thickness)
cv2.line(image,(50,50),(688,477),(0,0,255),2)
# Rectangle
cv2.rectangle(image,(100,400),(300,100),(255,0,0),2)

cv2.imshow("Frame",image)
cv2.waitKey(0)