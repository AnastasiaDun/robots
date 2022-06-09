import cv2 as cv

image = cv.imread('Image.png')
sample = cv.imread('sample.png')
image_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
lab_image = cv.cvtColor(image, cv.COLOR_BGR2LAB)
yCrCb_image = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)

imageH = image_hsv[:, :, 0]
imageS = image_hsv[:, :, 1]
imageV = image_hsv[:, :, 2]

def click_event(event, x, y, flags, params):
   global h, s, v, isTrue
   if event == cv.EVENT_LBUTTONDOWN:
       print('x - ', x, ', y - ', y)

       b = image[y, x, 0]
       g = image[y, x, 1]
       r = image[y, x, 2]

       h = image_hsv[y, x, 0]
       s = image_hsv[y, x, 1]
       v = image_hsv[y, x, 2]

       isTrue = True

       print('r - ', r, ', g - ', g, ',b - ', b)
       print('h - ', h, ', s - ', s, ', v - ', v)


cv.imshow('image', image)
cv.imshow('lab', lab_image)
cv.imshow('YCrCb', yCrCb_image)
cv.imshow('hsv_image', image_hsv)
cv.setMouseCallback('hsv_image', click_event)

cv.imshow('hue_image', imageH)
cv.imshow('saturation_image', imageS)
cv.imshow('value_image', imageV)

def Pass(x):
   pass

cv.createTrackbar('Value', 'hsv_image', 0, 255, Pass)

global isTrue
isTrue = False

while True:
   cv.imshow('hsv_image', image_hsv)
   image_hsv[:, :, 2] = cv.getTrackbarPos('Value', 'hsv_image')

   if isTrue:

       rgb = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
       lab = cv.cvtColor(rgb, cv.COLOR_BGR2LAB)
       yCrCb = cv.cvtColor(rgb, cv.COLOR_BGR2YCrCb)

       cv.imshow('hsv', hsv)
       cv.imshow('rgb', rgb)
       cv.imshow('lab', lab)
       cv.imshow('yCrCb', yCrCb)

       isTrue = False
   cv.waitKey(1)
