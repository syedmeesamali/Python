import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to input image")
ap.add_argument("-p", "--prototext", required = True, help = "path to caffe 'deploy' prototext file")
ap.add_argument("-m", "--model", required = True, help = "path to caffe pre-trained model")
ap.add_argument("-c", "--confidence", type = float, default = 0.5, 
        help = "minimum probability to filter weak detections")
args = vars(ap.parse_args())

print("[INFO] loading model ...")
net = cv2.dnn.readNetFromCaffe(args["prototext"], args["model"])

#Load image and construct an input blob
image = cv2.imread(args["image"])
(h, w)  = image.shape[:2]
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300,300)), 1.0, (300,300), (104.0, 177.0, 123.0))

print("[INFO] computing object detections ...")
net.setInput(blob)
detections = net.forward()

