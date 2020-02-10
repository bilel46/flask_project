import qrcode
import cv2
import numpy as np


def resize_b(image):
    a = 240
    img_x = np.ones((a,a,3), np.uint8)
    img_x[:,:,0] = cv2.resize(image[:,:,0],(a,a))
    img_x[:,:,1] = cv2.resize(image[:,:,1],(a,a))
    img_x[:,:,2] = cv2.resize(image[:,:,2],(a,a))
    return img_x

def resize_c(image,a,b):
    img_x = np.ones((a,b,3), np.uint8)
    img_x[:,:,0] = cv2.resize(image[:,:,0],(b,a))
    img_x[:,:,1] = cv2.resize(image[:,:,1],(b,a))
    img_x[:,:,2] = cv2.resize(image[:,:,2],(b,a))
    return img_x
"""

def creat_cart(data = "24685795",nom = 'rachdi',prenom = 'zinou',tel = '0697720846'):
    # creat and save qrimage
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 10,
        border = 4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image() 
    img.save("image.jpg") 
    # load qrimage and creat card
    cart = cv2.imread('cart.png')
    code = cv2.imread('image.jpg')
    logo = cv2.imread('logo_good.png')
    face = cv2.imread('faces\\'+data+'.jpg')
    code = resize_b(code)
    logo = resize_c(logo,100,200)
    face = resize_c(face,200,200)
    cart[10:250,566:806,:] = code
    cart[10:110,10:210,:] = logo
    cart[10:210,246:446,:] = face
    font = cv2.FONT_HERSHEY_SIMPLEX
    cart = cv2.putText(cart,nom,(245,330), font, 1,(255,255,255),2,cv2.LINE_AA)
    cart = cv2.putText(cart,prenom,(245,370), font, 1,(255,255,255),2,cv2.LINE_AA)
    cart = cv2.putText(cart,tel,(590,478), font, 1,(255,255,255),2,cv2.LINE_AA)
    # save card
    cv2.imwrite('cart1.png',cart)
    
    cv2.imshow('card',cart)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#creat_cart()


"""


    
import pyzbar.pyzbar as pyzbar

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

while True:
    _, frame = cap.read()

    obj = pyzbar.decode(frame)
    
    if len(obj)>0:
        obj = obj[0]
        #print("Data", obj.data)
        cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                    (255, 0, 0), 3)

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

a = (str(obj.data))[2:11]

print(a)
    
    

    
    
    
    
    

















    