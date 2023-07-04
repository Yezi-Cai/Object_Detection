import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)  # 0 is the default camera
# Check if the camera is opened successfully
if not cap.isOpened():
  print("Cannot open camera")
  exit()

# Start a loop to continuously capture frames from the camera
while True:
  # Capture frame-by-frame
  ret, frame = cap.read() # ret is true if the frame is available
                          # frame is an image array vector
  # Check if the frame was captured successfully
  if not ret:
    print("Can't receive frame (stream end?). Exiting ...")
    break

  # Display the resulting frame
  cv.imshow('frame', frame)  #imshow(<window name>, <image data>)

  # Exit the loop if 'q' is pressed
  if cv.waitKey(1) == ord('q'):  # waitKey(1) displays frame for 1ms
    break                        # ord('q') returns the Unicode code point of 'q'

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
