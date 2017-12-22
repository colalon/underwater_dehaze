import cv2
import numpy as np
import matplotlib.pyplot as plt
import dehaze
import time

cap = cv2.VideoCapture('05_20160415_114432.mp4')

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter( '05_20160415_114432_rehaze.avi',fourcc, 25.0, (704,480) )
i=0
ret = True
while( cap.isOpened() and ret == 1):
    start = time.time()
    print (i)
    ret, frame = cap.read()
    frame = np.float64(frame)
    frame = frame/255
    result = dehaze.dehaze(frame,1,15)
    
    result = np.uint8(result)
    cv2.imwrite('in.jpg',frame*255)
    cv2.imwrite('re.jpg',result)
    out.write(result)
    i=i+1
    print (time.time()-start)