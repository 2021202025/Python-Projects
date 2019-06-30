import cv2, time

video=cv2.VideoCapture(0)


while True:
    check, frame = video.read()
    print(check, frame)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # time.sleep(2)
    cv2.imshow("Capture", gray)

    key=cv2.waitKey(10)

    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()