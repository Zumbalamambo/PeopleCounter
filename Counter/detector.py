from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
import json
import time

def analyzeImg( imagePath ):

    image = cv2.imread(imagePath)
    image = imutils.resize(image, width=min(400, image.shape[1]))

    hogDesc = cv2.HOGDescriptor()
    hogDesc.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    (rects, weights) = hogDesc.detectMultiScale(image, winStride=(4, 4),padding=(8, 8), scale=1.05)

    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

    for (xA, yA, xB, yB) in pick:
        cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)

    newPath = "Counter/static/images/" + imagePath[5:]
    cv2.imwrite( newPath, image )

    filename = imagePath[imagePath.rfind("/") + 1:]
    return {'path':newPath[8:], 'count':len(pick)}
