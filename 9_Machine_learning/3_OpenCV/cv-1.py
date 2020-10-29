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

#Example usage: python cv-1.py 
# -i "./rsrc/rooster.jpg" -p "./rsrc/deploy.prototxt.txt" -m "./rsrc/res10_300x300_ssd_iter_140000.caffemodel"

print("[INFO] loading model ...")
net = cv2.dnn.readNetFromCaffe(args["prototext"], args["model"])

#Load image and construct an input blob
image = cv2.imread(args["image"])
(h, w)  = image.shape[:2]
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300,300)), 1.0, (300,300), (104.0, 177.0, 123.0))

print("[INFO] computing object detections ...")
net.setInput(blob)
detections = net.forward()

#loop over the detections
for i in range(0, detections.shape[2]):
        #extract confidence associated with the prediction
        confidence = detections[0, 0, i, 2]

        #filter out weak confidence
        if confidence > args["confidence"]:
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                #draw the bounding box for the detected face / shape
                text = "{:.2f}%".format(confidence * 100)
                y = startY - 10 if startY - 10 > 10 else startY + 10
                cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
                cv2.putText(image, text, (startX, y), cv2.FONT_HERSHEY_COMPLEX, 0.45, (0, 0, 255), 2)

#show the output image
cv2.imshow("Output", image)
cv2.waitKey(0)