import cv2, time

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

check, frame = video.read()

time.sleep(3)

video.release()
cv2.destroyAllWindows()