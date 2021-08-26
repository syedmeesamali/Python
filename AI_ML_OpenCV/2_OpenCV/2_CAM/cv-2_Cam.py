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
print("[INFO] Loading model ...")
net = cv2.dnn.readNetFromCaffe(args["prototext"], args["model"])

#Initialize vidoe stream and let camera setup warmup
print("[INFO] Starting video stream ...")
vs = VideoStream(src = 0).start()
time.sleep(2.0)

#Loop over frames from the video stream
while True:
    frame = vs.read()
    frame = imutils.resize(frame, width = 400)

    #Grab frame dimensions and convert it to a blob
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))

    #Pass the blob through neural network and obtain detections and predictions
    net.setInput(blob)
    detections = net.forward()

    #Loop over the detections
    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        #filter for confidence greater than minimum
        if confidence < args["confidence"]:
            continue

        #computer (x,y) of the bounding box
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")

        #draw bounding box along with associated probability
        text = "{:.2f}%".format(confidence * 100)
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 2)
        cv2.putText(frame, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

        #show the output frame
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        #if q was pressed then break from loop
    
#do the cleanup
cv2.destroyAllWindows()
vs.stop()
