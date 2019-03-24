import numpy as np
import cv2
import time
from matplotlib import pyplot as plt
import math

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_EXPOSURE, -13)
i = 0
while(True):
    # Capture frame-by-frame, 1 images per second
    time.sleep(1) 
    ret,frame = cap.read()
    cv2.imshow('frame',frame)
    i = i+1
    # Our operations on the frame come here
    # Chop the image to approciate size
    image = frame[150:450, 300:500]
    # Covert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Using threshold to convert the image to binary scale
    thresh1 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    # Find circles in the image
    circles = cv2.HoughCircles(thresh1, cv2.HOUGH_GRADIENT, 1, 7,
                               param1=60, param2=29, minRadius=0, maxRadius=40)
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # draw the outer circle
        cv2.circle(gray, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv2.circle(gray, (i[0], i[1]), 2, (0, 0, 255), 3)
    print(circles)
    Center_x_1 = circles[0][0][0]

    print('x coordinate of first LED')
    print(Center_x_1)
    Center_x_2 = circles[0][1][0]
    print('x coordinate of second LED')
    print(Center_x_2)
    # Find middle point between two LEDs for checking the buggy is moving on straight line
    middle_point = (np.absolute(Center_x_2-Center_x_1)/2)+Center_x_1
    print(middle_point)
    # The first middle point is needed to be stored into a parameter and the others will be compared with the first one

    # Find the distance
    Pixels = np.absolute(Center_x_2-Center_x_1)
    # Distance between two led is 21 cm, d is the half of that distance
    d = 10.5
    # The average pixels per degree is 29.8
    Pixel_per_degree = 29.8
    angle_in_rad = math.radians(Pixels/Pixel_per_degree)
    tan_angle = math.tan(angle_in_rad)
    distance = d/tan_angle
    print("The distance between camera and beacon is (mm)")
    print(distance)

    # Display the resulting frame
    cv2.namedWindow('detected circle')
    cv2.imshow('detected circle', gray)
    cv2.waitKey(0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
