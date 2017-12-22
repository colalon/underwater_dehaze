import cv2
import numpy as np
import matplotlib.pyplot as plt
import dehaze
import time

def nor(im):
    min=im.min()
    max=im.max()
    
    tim = 255*( (im-min)/(max-min) )
    
    return tim

cap = cv2.VideoCapture('ch5_12.avi')

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter( 's1.avi',fourcc, 25.0, (640,480) )
out2 = cv2.VideoWriter( 's2.avi',fourcc, 25.0, (640,480) )
i=0
ret = True
ret, frame = cap.read()
old = frame
while( cap.isOpened() and ret == 1):
    start = time.time()
    print (i)
    ret, frame = cap.read()
    frame = np.float64(frame)
    old = np.float64(old)
    fabs = abs(frame - old)
    ff = frame - old
    
    result1 = nor(fabs)
    result2 = nor(ff)
    
    result1 = np.uint8(result1)
    result2 = np.uint8(result2)
    cv2.imwrite('in.jpg',frame)
    cv2.imwrite('re1.jpg',result1)
    cv2.imwrite('re2.jpg',result2)
    out.write(result1)
    out2.write(result2)
    old = frame
    i=i+1
    #print (time.time()-start)