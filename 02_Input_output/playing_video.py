import os
import cv2

video_path=os.path.join("..","videos","v1.mp4")

video=cv2.VideoCapture(video_path)

# as considering 25 frames per second so 1/25 =40ms

ret=True
while(ret):
    ret,frame=video.read()
    if(ret):
        cv2.imshow("frame",frame)
        cv2.waitKey(20)
video.release()
cv2.destroyAllWindows()