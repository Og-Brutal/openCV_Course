import cv2
import os 


image =cv2.imread(os.path.join("..","Images","white_board.png"))
print(image.shape)
# Line
# cv2.line(image,(x,y),(x,y),(color),thickness)
cv2.line(image,(50,50),(688,477),(0,0,255),2)
# Rectangle
# cv2.rectangle(image,(120,250),(300,400),(255,0,0),2)
cv2.rectangle(image,(120,250),(300,400),(255,0,0),-1)

# circle
cv2.circle(image,(450,150),80,(0,255,0),30)


#text
cv2.putText(image,"Hello",((image.shape[1]//2)-30,20),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,255),2) 

cv2.imshow("Frame",image)
cv2.waitKey(0)




# Corner	Formula
# Top-Left	(min(x1,x2), min(y1,y2))
# Top-Right	(max(x1,x2), min(y1,y2))
# Bottom-Left	(min(x1,x2), max(y1,y2))
# Bottom-Right	(max(x1,x2), max(y1,y2))



# Parameter	Meaning
# image	Image where circle will be drawn
# center	Center point of the circle (x, y)
# radius	Radius of the circle
# color	Color in BGR
# thickness	Border thickness