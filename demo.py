import cv2
import numpy as np
import matplotlib.pyplot as plt
import dehaze
import time

start = time.time()

im = cv2.imread('demo.png')/255.0

result = dehaze.dehaze(im,1,15)

result = np.uint8(result)

cv2.imwrite('result.png',result)

print ('time:',time.time()-start)
