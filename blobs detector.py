import cv2
import numpy as np
from matplotlib import pyplot as plt
 
# Read image
original_image = cv2.imread("./70cm.jpg")
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

# is_v2 = cv2.__version__.startswith("2.")
# if is_v2:
#     detector = cv2.SimpleBlobDetector()
# else:
#     detector = cv2.SimpleBlobDetector_create()
 
# Set up the detector with default parameters.
# detector = cv2.SimpleBlobDetector()
 
# Detect blobs.
keypoints = detector.detect(mask)
im2 = 0
print(len(keypoints))
for marker in keypoints:
 im2 = cv2.drawMarker(original_image, tuple(int(i) for i in marker.pt),markerType=cv2.MARKER_STAR, color=(0, 0, 255))
plt.imshow(im2), plt.show()
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
# im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# Show keypoints
cv2.namedWindow('Keypoints')
cv2.imshow("Keypoints", im2)
cv2.waitKey(0)