import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("Cannot open camera")
    exit()
while True:
    _, out = cam.read()
    out2 = cv2.flip(out, 1)
    cv2.imshow("name", out2)

    # close the window_ _
    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
