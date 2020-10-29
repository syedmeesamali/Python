from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2

#Construct and parse and then parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototext", required=True, help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True, help="path to Caffe 'pre-trained' model")
ap.add_argument("-c", "--confidence", type=float, default=0.5, help="minimum probability")
args = vars(ap.parse_args())

#Load serialized model from disk