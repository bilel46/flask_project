
import numpy as np
import cv2

drawing = False 

exite_ = False
next_  = False
back_  = False
save_  = False
mask_  = False

font = cv2.FONT_HERSHEY_SIMPLEX
bo = True
alfa = 0

kernel = np.ones((10,10),np.uint8)

dog = "C:\\Users\\Public\\py_bilel_cv2\\dataset\\test_set\\dogs\\dog."
tx  = "C:\\Users\\Public\\py_bilel_cv2\\bouchoune\\x\\x"
ty  = "C:\\Users\\Public\\py_bilel_cv2\\bouchoune\\y\\y"


def draw_circle(event,x,y,flags,param):
    global drawing , next_ ,xb,yb,bo,exite_,back_,save_,mask_
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
            
    if event == cv2.EVENT_LBUTTONUP:
        drawing = False
        
    
    if 520<x<590 and 10<y<40 and drawing == True:
        exite_ = True
        
    if 520<x<590 and 60<y<90 and drawing == True:
        next_ = True
        
    if 520<x<590 and 110<y<140 and drawing == True:
        back_ = True
        
    if 520<x<590 and 160<y<190 and drawing == True:
        save_ = True
        
    if 520<x<590 and 210<y<240 and drawing == True:
        mask_ = True
        
        
    if 512<x<600 and drawing == True :
        bo = True


    if drawing == True and 0<x<512:
        print(bo)
        if bo == True:
            xb,yb = x,y
            bo = False
        cv2.line(img_main,(xb,yb),(x,y),(255,0,0),1)
        cv2.line(img_main,(xb+256,yb),(x+256,y),(255,0,0),1)
        xb,yb = x,y
        


def resize_b(image):
    img_x = np.ones((256,256,3), np.uint8)
    img_x[:,:,0] = cv2.resize(image[:,:,0],(256,256))
    img_x[:,:,1] = cv2.resize(image[:,:,1],(256,256))
    img_x[:,:,2] = cv2.resize(image[:,:,2],(256,256))
    return img_x

def resize_c(image):
    img_x = np.ones((128,128,3), np.uint8)
    img_x[:,:,0] = cv2.resize(image[:,:,0],(128,128))
    img_x[:,:,1] = cv2.resize(image[:,:,1],(128,128))
    img_x[:,:,2] = cv2.resize(image[:,:,2],(128,128))
    return img_x

def x_to_main(img_x,img_main):
    img_main[0:256,0:256,:] = img_x
    return img_main

def y_to_main(img_y,img_main):
    img_main[0:256,256:512,:] = img_y
    return img_main

def reg_main():
    img_main = np.zeros((256,600,3), np.uint8)#512
    img_main[10:40,520:590,2]=255
    img_main[:,513:515,1]=255
    return img_main

def cta_main(img_main):
    img_main[:,515:600,:]=(0,0,0)
    img_main[10:40,520:590,:]=(0,0,255)
    img_main[:,513:515,1]=255
    
    img_main[60:90,520:590,:  ]=255
    cv2.putText(img_main,'next',(520,85), font, 1,(255,0,0),1,cv2.LINE_AA)
    
    img_main[110:140,520:590,:]=255
    cv2.putText(img_main,'back',(520,135), font, 1,(255,0,0),1,cv2.LINE_AA)
    
    img_main[160:190,520:590,:]=255
    cv2.putText(img_main,'save',(520,185), font, 1,(255,0,0),1,cv2.LINE_AA)
    
    img_main[210:240,520:598,:]=255
    
 
    return img_main

  
img_x = np.zeros((256,256,3), np.uint8)
img_y = np.zeros((256,256,3), np.uint8)
img_main = reg_main()

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)



ind = 0

while(1):
    


    if next_ == True : 
        alfa += 1 
        sr = tx+str(alfa)+".png"
        image = cv2.imread(sr)
        image = resize_b(image)
        img_main = x_to_main(image,img_main)  

        img_main[0:256,256:512,:] = 0
        next_ = False  

    if back_ == True :
        alfa -= 1 
        image = cv2.imread(tx+str(alfa)+".png")
        image = resize_b(image)
        img_main = x_to_main(image,img_main)  

        img_main[0:256,256:512,:] = 0
        back_ = False 

    if save_ == True : 
        #cv2.imwrite(tx+str(ind)+".png",image                    )
        sr = ty+str(ind)+".png"
        cv2.imwrite(sr,resize_c(img_main[0:256,256:512,:]))
        ind += 1
        save_ = False
        print(alfa,"saved")
        
    if mask_ == True : 
        im_in = img_main[0:256,256:512,0]
        
        th, im_th = cv2.threshold(im_in, 127, 255, cv2.THRESH_BINARY)

# Copy the thresholded image
        im_floodfill = im_th.copy()

# Mask used to flood filling.
# NOTE: the size needs to be 2 pixels bigger on each side than the input image
        h, w = im_th.shape[:2]
        mask = np.zeros((h+2, w+2), np.uint8)

# Floodfill from point (0, 0)
        cv2.floodFill(im_floodfill, mask, (0,0), 255)

# Invert floodfilled image
        im_floodfill_inv = cv2.bitwise_not(im_floodfill)

# Combine the two images to get the foreground
        img_main[0:256,256:512,0] = im_th | im_floodfill_inv
        
        mask_ = False
        
        
        bo=True

    if exite_ == True :
        break

        
        

    cv2.imshow('image',img_main)
    img_main = cta_main(img_main)
    cv2.putText(img_main,str(alfa),(520,235), font, 1,(255,0,0),1,cv2.LINE_AA)
   
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        img[20:340,70:440,:] = 0


    
cv2.destroyAllWindows()





















