import cv2
import numpy as np
import serial
import time

ser=serial.Serial('COM6', 2000000)

# For OpenCV2 image display
WINDOW_NAME = 'GreenBallTracker' 


def track(image):

    '''Accepts BGR image as Numpy array
       Returns: (x,y) coordinates of centroid if found
                (-1,-1) if no centroid was found
                None if user hit ESC
    '''

    # Blur the image to reduce noise
    blur = cv2.GaussianBlur(image, (5,5),0)

    cv2.line(image, (0,240),(640,240), (0,0,255), 2)
    
    # Convert BGR to HSV
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    

    # Threshold the HSV image for only green colors
    lower_green = np.array([40,70,70])
    upper_green = np.array([80,200,200])

    # Threshold the HSV image to get only green colors
    mask = cv2.inRange(hsv, lower_green,upper_green)

    
    # Blur the mask
    bmask = cv2.GaussianBlur(mask, (5,5),0)

    # Take the moments to get the centroid
    moments = cv2.moments(bmask)
    m00 = moments['m00']
    centroid_x, centroid_y = None, None
    if m00 != 0:
        centroid_x = int(moments['m10']/m00)
        centroid_y = int(moments['m01']/m00)

    # Assume no centroid
    ctr = (-1,-1)

    # Use centroid if it exists
    if centroid_x != None and centroid_y != None:

        ctr = (centroid_x, centroid_y)

        # Put black circle in at centroid in image
        cv2.circle(image, ctr, 4, (0,0,0))
        val = centroid_y - 240
        #mal =(val + 500)
        mal = (centroid_y/2)
        tal = int(mal)
       # int (mal)
        print([centroid_x] ,[centroid_y],[val], [mal], [tal])
  	  #   cv2.line(image, (0, 100),(100,640), (255,0,0), 2)
     #   cv2.line(image, (centroid_x, centroid_y),(centroid_x,240), (255,0,0), 2)
        cv2.line(image, (centroid_x, centroid_y),(centroid_x,240), (255,0,0), 2)

        cv2.rectangle(image,(50,100),(590,380),(0,255,0),2)
        ser.write(bytes([tal]))
       # ser.write(mal)
       
       # ser.write(str(chr(mal)).encode())
       # serialcmd = input("n")
       # ser.write('K'.encode())
     #   serialcmdw()
       # port.write(serialcmd)
        
        
      #  ser.write('nn')
      #  ser.read(mal)
     #   time.sleep(1)
        
        cv2.putText(image,str(val), (centroid_x,centroid_y), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2)           
    # Display full-color image
    cv2.imshow(WINDOW_NAME, image)
    cv2.imshow('mask', bmask)
    # Force image display, setting centroid to None on ESC key input
    if cv2.waitKey(1) & 0xFF == 27:
        ctr = None
    
    # Return coordinates of centroid
    
    return ctr

# Test with input from camera
if __name__ == '__main__':

    capture = cv2.VideoCapture(0)
    #capture.set(cv2.c.CV_CAP_PROP_FPS, 60)
   # frame_rate = capture.get(cv2.cv.CV_CAP_PROP_FPS)
    while True:

        okay, image = capture.read()

        if okay:

            if not track(image):
                break
          
            if cv2.waitKey(1) & 0xFF == 27:
                break

        else:

           print('Capture failed')
           break
