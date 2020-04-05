import cv2

camera =cv2.VideoCapture(0)
while (camera.isOpened()):
    status,frame= camera.read()
    assert status,"cant read camera"
    grey= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("color",frame)
    cv2.imshow("grey", grey)
    if cv2.waitKey(1)==ord('q'):
        break


camera.release()
cv2.destroyAllWindows()