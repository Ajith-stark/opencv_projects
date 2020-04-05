import cv2 as cv
import numpy as np
path="/home/ajith/test/lib/python3.6/site-packages/cv2/data/"
face_cascade =cv.CascadeClassifier(path+'haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(path+'haarcascade_eye.xml')
camera = cv.VideoCapture(0)
print('PRESS Q to QUIT')

while True:
    status ,frame = camera.read()
    assert status,"error cant read"
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    # print(gray)
    faces= face_cascade.detectMultiScale(gray)
    for (x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h , x:x+w]
        roi_color = frame[y:y+
        eyes= eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv.imshow('color frame',frame)
    if cv.waitKey(1)==ord('q'):
        break
camera.release()
cv.destroyAllWindows()