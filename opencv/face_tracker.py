import cv2
import face_recognition

# video = cv2.VideoCapture(0) $ Webcam
video = cv2.VideoCapture("video.mp4")

frame_count = 0
faces = []

cv2.namedWindow("Face Tracker", cv2.WINDOW_NORMAL)

cv2.setWindowProperty(
    "Face Tracker",
    cv2.WND_PROP_FULLSCREEN,
    cv2.WINDOW_FULLSCREEN
)

while True:
    ret, frame = video.read()

    if not ret:
        break

    frame_count += 1

    if frame_count % 3 == 0:
        small = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        rgb = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)

        detected = face_recognition.face_locations(
            rgb,
            model="hog"
        )

        faces = [
            (
                top * 4,
                right * 4,
                bottom * 4,
                left * 4
            )
            for top, right, bottom, left in detected
        ]

    for top, right, bottom, left in faces:
        center_x = (left + right) // 2
        center_y = (top + bottom) // 2

        radius = max(right - left, bottom - top) // 2 + 20

        cv2.circle(
            frame,
            (center_x, center_y),
            radius,
            (0, 255, 0),
            3
        )

    cv2.imshow("Face Tracker", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
