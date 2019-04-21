import cv2

import numpy as np

from matplotlib import pyplot as plt

import math

import time

def blob():
# def blob(im,ary):

    # Read image
    original_image = cv2.imread("./50cm.jpg")
    im =cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)



    ret,mask = cv2.threshold(im, 240, 255, cv2.THRESH_TOZERO)

    mask = cv2.GaussianBlur(mask,(9,9),0)

    cv2.imshow("mask", mask)

    # Setup SimpleBlobDetector parameters.

    params = cv2.SimpleBlobDetector_Params()



    # Change thresholds



    params.filterByColor = True;

    params.blobColor = 255



    params.minThreshold = 240

    params.maxThreshold = 255;

    params.thresholdStep=2;

    # Filter by Area.

    params.filterByArea = True

    params.minArea = 5



    # Filter by Circularity

    params.filterByCircularity = True

    params.minCircularity = 0.7



    # Filter by Convexity

    params.filterByConvexity = True

    params.minConvexity = 0.87



    # Filter by Inertia

    params.filterByInertia = True

    params.minInertiaRatio = 0.5



    # Create a detector with the parameters

    ver = (cv2.__version__).split('.')

    if int(ver[0]) < 3 :

        detector = cv2.SimpleBlobDetector(params)

    else :

        detector = cv2.SimpleBlobDetector_create(params)





        # Detect blobs.

        keypoints = detector.detect(mask)

        im2 = 0

        print(len(keypoints))

        array=[]

        for marker in keypoints:

            im2 = cv2.drawMarker(original_image, tuple(int(i) for i in marker.pt),markerType=cv2.MARKER_STAR, color=(0, 0, 255))
            array.append(marker.pt)

        print(array)

        # calculate the middle point of the 2 reference leds for checking the buggy is moving on a straight line,
        # and put the middle points in to an array for calculation in the future
        # deviation = array_middle_point[len(array_middle_point)-1]-array_middle_point[0]
        # if deviation is larger than a certain value then output error

        array_middle_point =[]
        middle_point = (array[0][0]+array[1][0])/2
        array_middle_point.append(middle_point)

        print(array_middle_point)

        # Distance measurement code starts from here

        #Distance between two led is 21 cm, d is the half of that distance
        d=10.5
        #The average pixels per degree is 29.8
        Pixel_per_degree = 29.8

        Pixels = abs(array[0][0]-array[1][0])
        print(Pixels)

        angle_in_rad = math.radians(Pixels/Pixel_per_degree)
        tan_angle = math.tan(angle_in_rad)
        distance = d/tan_angle
        print("The distance between camera and beacon is (mm)")
        print (distance)

        # Distance measurement code finishes from here

        # ary.append(array)

        plt.imshow(im2), plt.show()




        # Show keypoints

        cv2.namedWindow('Keypoints')

        cv2.imshow("Keypoints", im2)

        cv2.waitKey(0)

if __name__ == '__main__':
    blob()
