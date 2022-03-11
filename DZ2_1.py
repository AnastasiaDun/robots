import numpy as np

import math

import cv2
points = []
plength: float = 0
scale: float = 3.2
end: bool = False

img = cv2.imread("/map.png")

def distance(a, b) :
    return math.sqrt((math.pow(a[0]-b[0],2) + (math.pow(a[1] - b[1], 2))))


def drawcircle (event, x,y, flags, param):
    global plength, img

    if end:
        return
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x, y), 2, (0, 255, 0), -1)
        points.append((x,y))

        if len(points) > 1:
            cv2.line (img, points[len(points) - 1], points[len(points) - 2],(0, 0, 255), 2)
            plength += distance(points[len(points)-1], points[len(points)-2])



cv2.namedWindow('map')
cv2.setMouseCallback('map', drawcircle)

while True:
    cv2.imshow('map', img)
    key = cv2.waitkey(1) & 0xFF

    if key == ord('s'):
        if not end:
            cv2.putText(img, f"{int(plength * scale)}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 144, 144), 2,
                        cv2.LINE_AA)

            enddraw = True

        if key == ord('q'):
            break

        cv2.waitkey(0)






