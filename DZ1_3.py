import cv2 as cv

capture = cv.VideoCapture(0)

fourcc = cv.VideoWriter_fourcc(*'XVID')
fps = 60
res = (640, 480)

path = 'new.mp4'
video_writer = cv.VideoWriter(path, fourcc, fps, res)


while True:
 ret, frame = capture.read()
 if ret:
    cv.imshow ('webcam', frame)
    video_writer.write(frame)

 if cv.waitKey(1) == 27:
    break


capture.release()
video_writer.release()

cv.destroyAllWindows()
