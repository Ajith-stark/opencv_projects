import cv2 as cv
import numpy as np

camera = cv.VideoCapture(0)
status,frame1= camera.read()
status,frame2= camera.read()
while camera.isOpened():
    diff= cv.absdiff(frame1,frame2)
    gray= cv.cvtColor(diff,cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray,(5,5),0)
    _,thresh= cv.threshold(blur,30,255,cv.THRESH_BINARY)
    dilated= cv.dilate(thresh,None,iterations=3)
    contours,_=cv.findContours(dilated,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x,y,w,h)=cv.boundingRect(contour)
        if cv.contourArea(contour) < 700:
            continue
        cv.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)

    cv.imshow("preview", frame1)
    frame1=frame2
    ret,frame2=camera.read()
    if cv.waitKey(1)==ord('q'):
        break


camera.release()
cv.destroyAllWindows()