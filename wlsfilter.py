import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.sparse import spdiags

im = cv2.imread('e_bw.jpg',0)
im = np.float64(im)
blur = cv2.blur(im,(15,15))

m,n = im.shape 

f=m*n/40000
f=np.sqrt(f)

r = int(np.ceil(m/f))
c = int(np.ceil(n/f))

im = cv2.resize(im,(c,r))
blur = cv2.resize(blur,(c,r))

lamda = 1.0 
alpha = 1.2

smallNum = 0.0001

r,c = im.shape 
k = int(r*c)
dy = np.zeros(im.shape)
dx = np.zeros(im.shape)

dy[0:r-1] = im[1:r] - im[0:r-1]
dy[r-1] = dy[r-2]
dy = -lamda/(abs(dy)*alpha + smallNum )
dy = dy.transpose()
dy=np.reshape(dy,(1,r*c))

dx[:,0:c-1] = im[:,1:c] - im[:,0:c-1]
dx[:,c-1] = dx[:,c-2]
dx = -lamda/(abs(dx)*alpha + smallNum )
dx = dx.transpose()
dx=np.reshape(dx,(1,r*c))

B = np.zeros((2,r*c))
B[0,:]=dx
B[1,:]=dy
d = np.array([-r,-1])

A=spdiags(B,d,k,k)

e = dx.copy()
w = e*0
w[0,r:k] = e[0,0:k-r] 
s = dy.copy()
n = s*0
n[0,r:k] = s[0,0:k-r] 

D=1-(e+w+s+n)

A = A + A.transpose() + spdiags(D, 0, k, k)
A = A.toarray()
#aa= np.resize(A,(1000,1000))
#ii = np.reshape(im,(k,1))

#result = np.linalg.solve(A,ii)

#result = A\ii