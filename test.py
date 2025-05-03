import cv2
import time
import datetime

video = cv2.VideoCapture(0) #sets camera
time.sleep(1)

while True:
    check, frame = video.read()
    date_string = datetime.datetime.now().strftime("%A %H:%M:%S")
    cv2.putText(frame, date_string, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("My Video",frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

video.release()