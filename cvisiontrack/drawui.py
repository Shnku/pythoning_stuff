import cv2
import tkinter as tk
from PIL import Image, ImageTk
import mediapipe as mp

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5,
)
mp_drawing = mp.solutions.drawing_utils

# Initialize drawing variables
drawing_color = "black"
drawing_thickness = 2
drawing = False
start_point = None


def draw(event):
    global start_point, drawing
    if drawing:
        x, y = event.x, event.y
        if start_point:
            canvas.create_line(
                start_point[0],
                start_point[1],
                x,
                y,
                fill=drawing_color,
                width=drawing_thickness,
            )
        start_point = (x, y)


def start_draw(event):
    global drawing, start_point
    drawing = True
    start_point = (event.x, event.y)


def stop_draw(event):
    global drawing, start_point
    drawing = False
    start_point = None


def clear_canvas():
    canvas.delete("all")



def update_frame():
    """
    Updates the Tkinter canvas with the latest frame from the OpenCV video stream
    and draws hand landmarks.
    """
    ret, frame = cam.read()
    if not ret:
        print("Cannot receive frame (stream end?). Exiting...")
        root.destroy()  # Close Tkinter window
        return

    # Process the frame with MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    # Draw hand landmarks on the frame (for displaying in OpenCV window)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
            )
            # Get tip of index finger.
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            h, w, c = frame.shape
            index_x, index_y = int(index_tip.x * w), int(index_tip.y * h)
            # Generate a Tkinter event.
            if drawing:
                canvas.event_generate("<B1-Motion>", x=index_x, y=index_y)

    # Convert the OpenCV frame to a PIL Image
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    # Convert the PIL Image to a Tkinter PhotoImage
    photo = ImageTk.PhotoImage(image=image)
    # Update the label's image
    video_label.config(image=photo)
    video_label.photo = photo  # Keep a reference!

    # Display the  OpenCV window
    cv2.imshow("Hand Tracking", frame) #show the opencv window

    # Schedule the next update
    video_label.after(15, update_frame)



# 1. Initialize OpenCV (video capture)
cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("Cannot open camera")
    exit()

# 2. Initialize Tkinter
root = tk.Tk()
root.title("Hand Tracking and Drawing")

# 3. Create a Label to display the video stream
video_label = tk.Label(root)
video_label.pack()

# 4. Create a Canvas for drawing
canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack(pady=10)

# Bind mouse events to the canvas for drawing
canvas.bind("<B1-Motion>", draw)  # Draw when left mouse button is dragged
canvas.bind("<ButtonPress-1>", start_draw)  # Start drawing on left mouse click
canvas.bind("<ButtonRelease-1>", stop_draw)  # Stop drawing when left mouse button is released

# 5. Create buttons for controls
clear_button = tk.Button(root, text="Clear Canvas", command=clear_canvas)
clear_button.pack()

# 6. Start the frame update loop
update_frame()

# 7. Run the Tkinter main loop
root.mainloop()

# 8. Release the video capture and close windows
cam.release()
cv2.destroyAllWindows()
hands.close()
