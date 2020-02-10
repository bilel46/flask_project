import threading
import cv2
import pyzbar.pyzbar as pyzbar
import time



def QRcode_scanner():  
    global frame,stop,QRcode
    stop=False
    
    cap = cv2.VideoCapture(1)
    font = cv2.FONT_HERSHEY_PLAIN
    i=1
    while(stop==False):
        time.sleep(0.03)
        _, frame = cap.read()
    
        obj = pyzbar.decode(frame)
        
        if len(obj)>0:
            obj = obj[0]
            
            cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                        (255, 0, 0), 3)
            QRcode = int((str(obj.data))[2:10])
            print(QRcode,i)            
            i=i+1
        print(i)
    cap.release()

    
t1 = threading.Thread(target=QRcode_scanner)
t1.start()
time.sleep(5)


while True:
          
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        stop = True
        break


cv2.destroyAllWindows()




