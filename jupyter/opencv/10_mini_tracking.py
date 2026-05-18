import cv2
import numpy as np

video_capture = cv2.VideoCapture(1)

while True:
    is_ok, frame = video_capture.read()
    if not is_ok:
        print("Fim do video!")
        break

    frame = cv2.resize(frame, None, fx=0.25, fy=0.25)

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([131, 0, 0])
    upper = np.array([159, 255, 168])
    mask = cv2.inRange(frame_hsv, lower, upper)

    contours, hier = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        c_area = cv2.contourArea(cnt)
        if c_area > 1200:
            peri = cv2.arcLength(cnt, True)
            approx_cnt = cv2.approxPolyDP(cnt, 0.1 * peri, True)
            x, y, w, h = cv2.boundingRect(approx_cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting image
    cv2.imshow('Video', frame)
    cv2.imshow('Mask', mask)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

video_capture.release() 
cv2.destroyAllWindows()
