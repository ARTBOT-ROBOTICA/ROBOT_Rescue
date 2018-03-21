# USAGE
# python motion_detector.py
# python motion_detector.py --video videos/example_01.mp4

# import the necessary packages
import argparse
import datetime
import imutils
import time
import cv2

camera = cv2.VideoCapture(1)
time.sleep(0.5)


# initialize the first frame in the video stream


# loop over the frames of the video
while True:

        (grabbed, frame) = camera.read()
        key = cv2.waitKey(1) & 0xFF
        
        text = "motionless"
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        if key == ord('m'):
                foto = frame
                cv2.imwrite("captura2.png",foto)
        firstFrame = cv2.imread('captura2.png')
        firstFrame= cv2.cvtColor(firstFrame, cv2.COLOR_BGR2GRAY)
        firstFrame = cv2.GaussianBlur(firstFrame, (21, 21), 0)
        #firstFrame= cv2.cvtColor(firstFrame, cv2.COLOR_BGR2GRAY)
        #gray = cv2.GaussianBlur(gray, (21, 21), 0)
        frameDelta = cv2.absdiff(firstFrame, gray)
        thresh = cv2.threshold(frameDelta, 50, 255, cv2.THRESH_BINARY)[1]

        # dilate the thresholded image to fill in holes, then find contours
        # on thresholded image
        thresh = cv2.dilate(thresh, None, iterations=3)
        (_,cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE)

        # loop over the contours
        for c in cnts:
                # if the contour is too small, ignore it
                if cv2.contourArea(c) < 50:
                        continue

                # compute the bounding box for the contour, draw it on the frame,
                # and update the text
                (x, y, w, h) = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                text = "movement"

        # draw the text and timestamp on the frame
        cv2.putText(frame, "Status: {}".format(text), (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 150, 0), 2)
        cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 150, 0), 1)

        # show the frame and record if the user presses a key
        cv2.imshow("Imagen base", frame)
        cv2.imshow("Seguimiento", thresh)
        cv2.imshow("Silueta", frameDelta)
        

        # if the `q` key is pressed, break from the lop
        if key == ord("q"):
                break

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
