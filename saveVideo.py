import cv2
camera = cv2.VideoCapture(0)
# codec and format of video file
fourcc = cv2.VideoWriter_fourcc(*'XVID')
framespersec = 40
height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
width= camera.get(cv2.CAP_PROP_FRAME_WIDTH)
print(height,width)
out =cv2.VideoWriter('output.avi',fourcc,framespersec,(640,480))
while (camera.isOpened()):
    status,frame= camera.read()
    assert status,"cant read camera"
    grey= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("video",frame)
    out.write(frame)
    # cv2.imshow("gerey", grey)
    if cv2.waitKey(1)==ord('q'):
        break


camera.release()
out.release()
cv2.destroyAllWindows()