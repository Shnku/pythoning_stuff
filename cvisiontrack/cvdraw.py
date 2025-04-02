import cv2 as cv
import numpy as np

blank_canvas = np.zeros((500, 800, 3), dtype=np.uint8)


def linedraw():
    cv.line(blank_canvas, (0, 39), (334, 56), (0, 250, 34), 3)


# Function to draw a circle
def draw_circle(canvas, center, radius):
    cv.circle(canvas, center, radius, (0, 255, 0), -1)


# Function to draw a rectangle
def draw_rectangle(canvas, pt1, pt2):
    cv.rectangle(canvas, pt1, pt2, (0, 0, 255), -1)


# Function to draw a line
def draw_line(canvas, start, end):
    cv.line(canvas, start, end, (255, 0, 0), 2)


# Draw elements on the canvas
draw_rectangle(blank_canvas, (100, 100), (400, 400))
draw_line(blank_canvas, (0, 450), (800, 450))
draw_circle(blank_canvas, (250, 250), 150)

linedraw()
cv.imshow("Blank Canvas", blank_canvas)
cv.waitKey(0)
cv.destroyAllWindows()
