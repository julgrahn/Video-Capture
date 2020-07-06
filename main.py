import cv2, time

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

a = 1

while True:
    a = a+1
    check, frame = video.read()

    print(check)
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)          #convert into gray image
    #time.sleep(3)
    cv2.imshow("Capturing", gray)

    keyPress = cv2.waitKey(1)
    if keyPress == ord('q'):
        break

print("Frames: ", a)
video.release()
cv2.destroyAllWindows()