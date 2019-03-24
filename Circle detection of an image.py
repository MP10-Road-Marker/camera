import numpy as np
import cv2
import time
from matplotlib import pyplot as plt

# Acquire and read the image
original_image = cv2.imread('./50cm.jpg')
hsv = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)
image = original_image[150:450, 300:500]
# Covert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

circle = original_image[335:360, 380:410]

lower_red = np.array([150, 0, 0])
upper_red = np.array([255, 100, 100])
mask = cv2.inRange(original_image, lower_red, upper_red)
cv2.imshow('circle', mask)
cv2.waitKey(0)
exit(0)

Hchannel = cv2.inRange(hsv[:,:,0],150 ,200)
Schannel = cv2.inRange(hsv[:,:,1],0,15)
Vchannel = cv2.inRange(hsv[:,:,2],230,255)
res = cv2.bitwise_and(Hchannel,Hchannel, mask= Schannel)
res = cv2.bitwise_and(res,res, mask= Vchannel)

cv2.imshow('Hchannel', Hchannel)
cv2.imshow('Vchannel', Vchannel)

cv2.waitKey(0)
exit(0)
frame = original_image

mask = cv2.inRange(Vchannel, 230, 255)

res = cv2.bitwise_and(frame,frame, mask= mask)

cv2.imshow('frame', frame)
cv2.imshow('mask', mask)
cv2.imshow('res', res)


# Using threshold to convert the image to binary scale
thresh1 = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# Another method of threshold
ret, th1 = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
# Find the edge of the image
edge = cv2.Canny(th1, 0, 0)
# Find circles in the image
circles = cv2.HoughCircles(thresh1, cv2.HOUGH_GRADIENT, 1,7, param1=60, param2=30, minRadius=0, maxRadius=50)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(gray,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(gray,(i[0],i[1]),2,(0,0,255),3)
print(circles)
Center_x_1 = circles[0][0][0]
print(Center_x_1)
Center_x_2 = circles[0][1][0]
print(Center_x_2)

# Creat windows
# cv2.namedWindow('1')
# cv2.namedWindow('2')
cv2.namedWindow('3')
cv2.namedWindow('4')
cv2.namedWindow('5')
# cv2.namedWindow('detected circles')

# cv2.imshow('1',image)
cv2.imshow('2', thresh1)
cv2.imshow('3', th1)
cv2.imshow('4', gray)
cv2.imshow('5', edge)
# cv2.imshow('detected circles',edge)

cv2.waitKey(0)
