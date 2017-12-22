import numpy as np

def get_stmosphere(im,dark_channel):
    
    m,n,k=im.shape
    
    n_search_pixels=int(np.floor(m*n*0.05))

    dark_vec = np.reshape(dark_channel,( m*n));
    image_vec = np.reshape(im, (m*n, 3));
    
    indices=np.argsort(dark_vec)
    accumulator = np.zeros((1,3))
    
    atm_map = image_vec.copy()
    #dark_map = dark_vec.copy()
    
    for k in range (int(m*n)-1,int(m*n)-n_search_pixels-1,-1):
        accumulator = accumulator + image_vec[indices[k]]
        atm_map[indices[k]]=1,0,0
    
    accumulator = accumulator / n_search_pixels
        
    test  = np.reshape(atm_map,im.shape)
    return accumulator , test