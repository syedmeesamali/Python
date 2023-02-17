from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time

#Construct the argument parse and then parse the argument
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to option video files")
ap.add_argument("-b", "--buffer", type=int, default=64, help="max buffer size")
args = vars(ap.parse_args())

#Define upper and lower boundaries of color of ball so it can be tracked
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
pts = deque(maxlen=args["buffer"])

#if video path not provided then switch to the webcam
if not args.get("video", False):
    vs = VideoStream(src=0).start()

#Otherwise grab reference to video file
else:
    vs = cv2.VideoCapture(args["video"])

#Allow camera on video file to warm-up
time.sleep(2.0)

#Keep the main loop
while True:
    frame = vs.read()           #Current frame
    frame = frame[1] if args.get("video", False) else frame
    if frame is None:
        break

    frame = imutils.resize(frame, width = 600)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    #Construct mask for the color green
    mask = cv2.inRange(hsv, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    
