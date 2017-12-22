import numpy as np

def get_dark_channel(im,win_size):
    
#im=np.random.random_sample((100,100,3))/2
#win_size=15
    
    m,n,k=im.shape
    pad_size = int(np.floor(win_size/2))
    
    padimage=np.ones((m+2*pad_size,n+2*pad_size,k))
        
    padimage[ pad_size:pad_size+m ,pad_size:pad_size+n]=im
    
    dark_channel = np.zeros((m,n))
    
    for i in range (0,m):
        for j in range (0,n):
            patch=padimage[i:i+win_size-1,j:j+win_size-1]
            dark_channel[i,j]=patch.min()
            
    return dark_channel