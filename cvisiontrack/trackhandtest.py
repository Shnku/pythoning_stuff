import cv2
import mediapipe as mp

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5,
)
mp_drawing = mp.solutions.drawing_utils

# Start video capture
cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("Cannot open camera")
    exit()

while True:
    _, out_frame = cam.read()
    if not _:
        print("Cannot receive frame (stream end?). Exiting ...")
        break
    # out_frame = cv2.flip(out_frame, 1)
    rgb_frame = cv2.cvtColor(out_frame, cv2.COLOR_BGR2RGB)

    # Process the out_frame and detect hands
    results = hands.process(rgb_frame)

    # Draw hand landmarks on the out_frame
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                out_frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
            )

    # Display the out_frame with hand landmarks
    cv2.imshow("Hand Tracking", out_frame)

    # Close the window if 'q' is pressed
    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
hands.close()

"""
  The code above initializes the Mediapipe Hands model and starts the video capture from the camera. 
  It then processes the video frame by frame and detects hands in the frame. 
  The detected hand landmarks are drawn on the frame and displayed in a window. The program will run until the 'q' key is pressed.
  To run the code, save it in a file named  track
"""
