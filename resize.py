

import cv2
import numpy as np


"""

def resize_c(image,a,b):
    img_x = np.ones((a,b,3), np.uint8)
    img_x[:,:,0] = cv2.resize(image[:,:,0],(b,a))
    img_x[:,:,1] = cv2.resize(image[:,:,1],(b,a))
    img_x[:,:,2] = cv2.resize(image[:,:,2],(b,a))
    return img_x


cart1 = cv2.imread('images\\nouveau.png')

# soutour amida
cart =  resize_c(cart1,450,400)

cv2.imshow('card',cart)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('images\\b_nouveau.png',cart)

"""
import time

def im():

    msg = np.zeros((100,450,3),dtype=np.uint8)
    
    msg[:,:,:]=(102, 102, 0)
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(msg,'Apuie la cart sur la came',(10,60), font, 1,(0,0,0),2,cv2.LINE_AA)

    cv2.imshow('msg',msg)
    
    time.sleep(3)

r=2  
#im()    

msg = np.zeros((100,450,3),dtype=np.uint8)

msg[:,:,:]=(102, 102, 0)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(msg,'Apuie la cart sur la came',(10,60), font, 1,(0,0,0),2,cv2.LINE_AA)

cv2.imshow('msg',msg)

if r ==1 :
    cv2.destroyAllWindows()
time.sleep(3)

#cv2.waitKey(0)
cv2.destroyAllWindows()








