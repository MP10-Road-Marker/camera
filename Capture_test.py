import numpy as np
import cv2
import time
from matplotlib import pyplot as plt
import sys 

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_EXPOSURE,-13)

while(True):
    ret, frame = cap.read()

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
sys.exit
