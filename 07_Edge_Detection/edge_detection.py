import os 
import cv2 
import numpy as np

image=cv2.imread(os.path.join("..","Images","basket_ball_player.png"))

edges_detected=cv2.Canny(image,100,200)

edges_detected_d=cv2.dilate(edges_detected,np.ones((3,3),dtype=np.int8))
edges_detected_e=cv2.erode(edges_detected,np.ones((3,3),dtype=np.int8))
cv2.imshow("player",image)
cv2.imshow("edges_detected",edges_detected)
cv2.imshow("edges_detected_d",edges_detected_d)
cv2.imshow("edges_detected_e",edges_detected_e)
cv2.waitKey(0)