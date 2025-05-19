# Week_1_Task_1_Solution

import cv2
import numpy as np

img = cv2.imread('/Users/priyanshumeena/Desktop/codes/o.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, threshold1=50, threshold2=150)
lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=100)

x_coords = []
y_coords = []

if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        x_coords.extend([x1, x2])
        y_coords.extend([y1, y2])

    x_coords = np.array(x_coords)
    y_coords = np.array(y_coords)

    # Get min and max points by coordinate values
    x_min = np.min(x_coords)
    y_min = np.min(y_coords)
    x_max = np.max(x_coords)
    y_max = np.max(y_coords)

    # Calculate slope between (x_min, y_min) and (x_max, y_max)
    if x_max - x_min == 0:
        slope = float('inf')
    else:
        slope = (y_max - y_min) / (x_max - x_min)

    print(f"Line coordinates: ({x_min}, {y_min}), ({x_max}, {y_max}), Slope: {slope}")
    
    # Show the line image
    line_img = np.zeros_like(img)
    cv2.line(line_img, (x_min, y_min), (x_max, y_max), (255, 0, 0), 2)
    cv2.imshow('Line', line_img)
else:
    print("No lines detected")

cv2.waitKey(0)
cv2.destroyAllWindows()