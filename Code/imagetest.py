import cv2
import os
import sys
import numpy as np


sys.path.append('/Users/seanmcauliffe/Desktop/Dev/repos/Fencing_App/openpose/build/python');
from openpose import pyopenpose as op

params = dict()
params["model_folder"] = "../openpose/models/"



opWrapper = op.WrapperPython()
opWrapper.configure(params)
opWrapper.start()
datum = op.Datum()

cap = cv2.imread(sys.argv[1])
datum.cvInputData = cap
opWrapper.emplaceAndPop([datum])

print("Body keypoints: \n" + str(datum.poseKeypoints))
print("Face keypoints: \n" + str(datum.faceKeypoints))
print("Left hand keypoints: \n" + str(datum.handKeypoints[0]))
print("Right hand keypoints: \n" + str(datum.handKeypoints[1]))
#cv2.imshow("Fencing_App", datum.cvOutputData)
cv2.imwrite('Test Image.png', datum.cvOutputData)


