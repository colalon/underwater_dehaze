import cv2
import numpy as np
import get_dark_channel
import get_atmosphere
import matplotlib.pyplot as plt
import UnderwaterColorCorrection


def dehaze(im,omega,win_size):    
    m,n=im.shape[:2]
    
    img = im.copy()
    
    img[:,:,2]=1-img[:,:,2]
    
    dark_channel = get_dark_channel.get_dark_channel(img,win_size)
    atmosphere , test = get_atmosphere.get_stmosphere(im,dark_channel)
    
    #plt.imshow(test)
    
    rep_atmosphere=atmosphere.copy()
    rep_atmosphere[0,2]=1-atmosphere[0,2]
    trans_est = 1 - omega * get_dark_channel.get_dark_channel(img/rep_atmosphere,win_size)
    
    transmission = trans_est.copy()
    
    #plt.imshow(transmission)
    transmission = cv2.blur(transmission,(15,15))
    
    #transmission = np.float32(transmission)
    #transmission = cv2.medianBlur(transmission,5)
    #transmission=cv2.bilateralFilter(transmission,9,75,75)
    transmission[transmission<0.3] = 0.3
    transmission[transmission>1] = 1
    
    #plt.imshow(transmission)
    
    #####################################
    radiance = im - atmosphere
    radiance[:,:,0] = radiance[:,:,0]/transmission[:,:]
    radiance[:,:,1] = radiance[:,:,1]/transmission[:,:]
    radiance[:,:,2] = radiance[:,:,2]/transmission[:,:]
    radiance = radiance + atmosphere
    
    
    radiance[radiance<0]=0;
    radiance[radiance>1]=1;
    #####################################
    
    ab_radiance = np.zeros(im.shape)
    ln_image = np.log(radiance+0.001)
    ln_trans = np.log(transmission+0.001)
    k=0.25
    beta_r=-np.log(atmosphere[0,2]/atmosphere.max())
    beta_g=-np.log(atmosphere[0,1]/atmosphere.max())
    beta_b=-np.log(atmosphere[0,0]/atmosphere.max())
    
    ab_radiance [:, :, 2] = np.exp(ln_image[:, :, 2] - beta_r*ln_trans)
    ab_radiance [:, :, 1] = np.exp(ln_image[:, :, 1] - beta_g*ln_trans)
    ab_radiance [:, :, 0] = np.exp(ln_image[:, :, 0] - beta_b*ln_trans);
    
    ab_radiance [ab_radiance <0]=0
    ab_radiance [ab_radiance >1]=1
    #######################################
    
    result=UnderwaterColorCorrection.UnderwaterColorCorrection( ab_radiance, 0.3 )
    
    result=result*255
    #cv2.imwrite('result.jpg',result)
    return result
'''
im=cv2.imread('b.jpg')
im=np.float64(im)
im=im/255
omega, win_size = 10 ,15

result=dehaze(im,omega,win_size)

result = np.uint8(result)

#result = result * 255

#plt.imshow(result)
cv2.imwrite('rr.jpg',result)
########################
'''
