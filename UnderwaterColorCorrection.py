import numpy as np

def UnderwaterColorCorrection( image, alpha ):
    m , n , k = image.shape
    
    im_gray = np.zeros((m,n))
    im_gray = 0.299*image[:,:,2]+0.587*image[:,:,1]+0.114*image[:,:,0]
    Lmean = im_gray.mean()
    eps = 0.001
    
    imgP = np.zeros(image.shape)
    
    for i in range (0,3):
        imgP[:,:,i] = np.power( ( im_gray / (image[:,:,i]+eps) ),alpha) * image[:,:,i]
        
    Pmeanr = imgP[:,:,2].mean()
    Pmeang = imgP[:,:,1].mean()
    Pmeanb = imgP[:,:,0].mean()
    
    result = imgP - [Pmeanb ,Pmeang ,Pmeanr] + Lmean 
    
    result[result<0]=0
    result[result>1]=1
    
    return result