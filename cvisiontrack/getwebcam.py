# import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    grey = cv.flip(frame, 1)
    # Display the resulting frame
    # cv.imshow("frame", frame)
    cv.imshow("frame", grey)
    if cv.waitKey(1) == ord("q"):
        break
cap.release()
cv.destroyAllWindows()

# Yes, that's correct! If you remove the line if cv2.waitKey(1) == ord("q"): from your OpenCV loop, the camera feed may not display properly, and the application can appear to be "stuck" or unresponsive. Here’s why this happens:
# Reasons for the Camera Feed Not Displaying Properly
#
#     Event Loop Handling:
#         The cv2.waitKey() function is crucial for processing GUI events. When you call cv2.imshow(), it displays the image in a window, but without cv2.waitKey(), the window may not refresh or respond to user inputs (like closing the window or pressing keys).
# The function allows OpenCV to handle window events, which is necessary for the display to update correctly.

# Frame Refresh:
# The cv2.waitKey() function introduces a small delay, allowing the program to pause briefly and give time for the window to update. If you don't include it, the loop runs continuously without any pause, which can lead to the display not updating as expected.

# High CPU Usage:
# Without cv2.waitKey(), the loop runs as fast as possible, consuming a lot of CPU resources. This can lead to performance issues, and the application may become unresponsive or behave erratically.
