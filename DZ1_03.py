from cv2 import cv2

import numpy as np

import os

import time


cap = cv2.VideoCapture(0)

out = cv2.VideoWriter('video.mp4', cv2.VideoWriter_fourcc(*'XVID'), 30.0, (640,480))

i = 0
while True:
	ret, frame = cap.read()
	out.write(frame)
	time.sleep(0.05)
	i = i + 1
	if i > 50:
		break

cap.release()
cv2.destroyAllWindows()


