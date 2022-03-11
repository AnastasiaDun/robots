import numpy as np

import math

import cv2
points = []
framesize = (int(video.get(3)), int(video.get(4)))
matrix = None
select:bool = False
firstRead:bool = True
video = cv2.VideoCapture("/Video.mp4")

def distance (a, b): return math.sqrt ((math.pow(a[0] -b[0], 2) + (math.pow(a[1] - b[1], 2))))

def drawcircle (event, x,y, flags, param):
    global select, matrix
    if len(points) == 4:
        width = distance(points[0], points[1])
        height = distance(points[1], points[3])

    pts1 = np.float32 ([[points[0]], [points[1]], [points[2]], [points[3]]])

    pts2 = np.float32 ([[framesize[0]/2 - width / 2, framesize[1] /2 - height/2],
                   [framesize[0]/2 - width / 2, framesize[1] /2 - height/2],
                    [framesize[0]/2 - width / 2, framesize[1] /2 + height/2],
                    [framesize[0]/2 - width / 2, framesize[1] /2 + height/2]
                   ])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    select = True
    return



    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x,y),2,(255,0,0), -1)
        points.appemd((x,y))

cv2.namedWindow('Show')
cv2.setMouseCallback('Show',drawcircle)


while video.isOpened():
    key = cv2.waitkey(2) & 0xFF
    if firstRead:
        res,img = video.read()
        cv2.imshow("Show", img)
        firstRead = False

    if select:
        res, img = video.read()
        if res:
            imgOutput = cv2.warpPerspective(img, matrix, framesize)
            cv2.imshow("Show", imgOutput)
        else:
            break


    if key == ord('q'):
        break

cv2.destroyAllWindows()

