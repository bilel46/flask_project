import cv2
import time

#cap = cv2.VideoCapture(1)
#
#
#
#def GetImage(qrcode):
#    global cap
#
#    while True:
#        _, frame = cap.read()
#    
#    
#        cv2.imshow("Appuyez sur s pour déposer l'image", frame)
#    
#        if cv2.waitKey(1) & 0xFF == ord('s'):
#            qr = str(qrcode)
#            cv2.imwrite('faces\\'+qr+'.png',frame)
#            break
#    cv2.destroyAllWindows()
#
#GetImage(10000000)
#cap.release()

#import time
#
#
#
#def mois2date(mois):
#    s = mois*30*24*60*60
#    s = time.time()+s+(3600*15)*mois
#    return s
#
#def fin(s):
#    t = time.localtime(s)
#    t = str(t[0])+'/'+str(t[1])+'/'+str(t[2])+'/'+'  '+str(t[3])+':'+str(t[4])
#    return t
#    
#
#au = time.localtime(time.time())
#
#t = mois2date(1)
#t = fin(t)
#print(t)




















import threading



def QRcode_scanner(): 
    
    global frame0,stop,QRcode
    stop=False
    QRcode=10000000
    
    cap = cv2.VideoCapture(1)
    while(stop==False):
        time.sleep(0.02)
        _, frame0 = cap.read()
        cv2.imshow("Frame_0", frame0)
        
            
#        print(i)
    cap.release()

    
t1 = threading.Thread(target=QRcode_scanner)
t1.start()






















