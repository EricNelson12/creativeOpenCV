import numpy as np
import cv2

cap = cv2.VideoCapture(0)

count = 50


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    kernel = np.ones((10,2),np.uint8)    
    
    # gray = cv2.dilate(gray,kernel,iterations = 1)

    kernel = np.ones((2,10),np.uint8)

    # gray = cv2.erode(gray,kernel,iterations = 3)

  


    gray = cv2.Canny(gray,count,count)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()