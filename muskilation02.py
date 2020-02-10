import wx
import qrcode
import cv2
import numpy as np
import threading
import time
import pyzbar.pyzbar as pyzbar
import sqlite3
from wx.lib import statbmp
from pygame import mixer


global QRcode

###########################################    database

def create_db(name='musculation.db'):
    conn = sqlite3.connect(name)
    conn.commit()
    conn.close()


def create_table(database_name='musculation.db',table_name='client',col=['nom text','prenom text','tel integer','date integer','qrcode integer','many integer','id integer']):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    com = "CREATE TABLE {} ("
    for i in col[0:len(col)-1]:
        com = com+i
        com = com+","
    com = com+col[len(col)-1]
    com = com+")"
    c.execute(com.format((table_name)))
    conn.commit()
    conn.close()
    insert_data(col_data=['bilel text','boumediene text','0697720832 integer','1577020979 integer','10000000 integer','0 integer','0 integer'])
    
def insert_data(database_name='musculation.db',table_name='client',col_data=['bilel text','boumediene text','0697720832 integer','1577020979 integer','00000000 integer','0 integer','0 integer']):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    com = "INSERT INTO {} VALUES ("
    for i in col_data[0:len(col_data)-1]:
        lene = len(i)
        if i[lene-4:]=="text":
            com = com+"'"+i[0:lene-5]+"'"
            com = com+","
        if i[lene-4:]=="eger":
            com = com+i[0:lene-8]
            com = com+"," 
    i = col_data[len(col_data)-1]
    lene = len(i)
    if i[lene-4:]=="text":
        com = com+"'"+i[0:lene-5]+"'"
    if i[lene-4:]=="eger":
        com = com+i[0:lene-8] 
    com = com+")"
        
    c.execute(com.format(table_name))
    conn.commit()
    conn.close() 

def selct_data(database_name='musculation.db',table_name='client',qrcode=25487595):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()    
    c.execute("SELECT * FROM {} WHERE qrcode={}".format(table_name,qrcode))
    p = c.fetchone()  
    return p

def update_date(database_name='musculation.db',table_name='client',qrcode=25487595,date=5564885):
    conn = sqlite3.connect(database_name)
    c = conn.cursor() 
    c.execute("UPDATE {} SET date = {} WHERE qrcode = {}".format(table_name,date,qrcode))    
    conn.commit() 
    conn.close() 

def update_many(database_name='musculation.db',table_name='client',qrcode=25487595,many=0):
    conn = sqlite3.connect(database_name)
    c = conn.cursor() 
    c.execute("UPDATE {} SET many = {} WHERE qrcode = {}".format(table_name,many,qrcode))    
    conn.commit() 
    conn.close() 
    
def creat_QRcode(database_name='musculation.db',table_name='client',id='0'):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()    
    c.execute("SELECT * FROM {} WHERE id={}".format(table_name,id))
    p = c.fetchall() 
    qrcodes = np.zeros((len(p)))
    v = 0
    for i in p:
        qrcodes[v] = i[4]
        v = v+1
    maxe = int((qrcodes).max()+1)
    return maxe

def musk_insert(nom,prenom,tel,date,qrcode,many,idi):
    insert_data(col_data=[nom+' text',prenom+' text',tel+' text',str(date)+' integer',str(qrcode)+' integer',str(many)+' integer',str(idi)+' integer'])

def mois2date(mois):
    s = mois*30*24*60*60
    t = time.time()+s+(3600*15)*mois
    return t

def fin(s):
    t = time.localtime(s)
    t = str(t[0])+'/'+str(t[1])+'/'+str(t[2])+'  '+str(t[3])+':'+str(t[4])
    return t



def selct_time(database_name='musculation.db',table_name='client',qrcode=25487595):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()    
    c.execute("SELECT * FROM {} WHERE qrcode={}".format(table_name,qrcode))
    p = c.fetchone()  
    return p[3]


###########################################    the end of database    24685795


###########################################    QRcode

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

# creat card fanction
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
    face = cv2.imread('faces\\'+data+'.png') # load face from folder faces
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
    cv2.imwrite('card\\'+data+'.png',cart)
    
    cv2.imshow('card',cart)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# QRcode tread ---> globel var QRcode
def QRcode_scanner():  
    global frame0,stop,QRcode,Trouve,qre
    Trouve=False
    stop=False
    QRcode=10000000
    qre = 10000000
    
    cap = cv2.VideoCapture(0)

    while(stop==False):
        time.sleep(0.02)
        _, frame0 = cap.read()
        
        obj = pyzbar.decode(frame0)
        
        if len(obj)>0:
            obj = obj[0]
            print(obj.data)
            if len(str(obj.data)) == 11:
                QRcode = int((str(obj.data))[2:10])
                
        if qre != QRcode :
            
            qre=QRcode
            Trouve=True
            
#        print(i)
    cap.release()

    
t1 = threading.Thread(target=QRcode_scanner)
t1.start()
time.sleep(5)

 #display frame
#while True:
#          
#    cv2.imshow("Frame", frame0)
#
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        stop = True
#        break


#cv2.destroyAllWindows()

def lire_qrcode():   
    font = cv2.FONT_HERSHEY_PLAIN
    
    for i in range(70):
        
        img = frame0
        obj = pyzbar.decode(img)
        img = resize_c(img,200,200)
        if len(obj)>0:
            obj = obj[0]
            cv2.putText(img, str(obj.data), (50, 3), font, 1,
                        (255, 0, 0), 2)
        cv2.imshow("B.m", img)
        
        
        if cv2.waitKey(1) & 0xFF == ord('l'):
            break       
        
        
        print(QRcode)
        time.sleep(0.1)
        
        if not(QRcode==10000000):
            cv2.destroyAllWindows()
            return QRcode
        
    cv2.destroyAllWindows()
    return False
    
        
            
        
def GetImage(qrcode):
    global cap

    while True:   
        
        cv2.imshow("Appuyez sur s pour déposer l'image", frame0)
    
        if cv2.waitKey(1) & 0xFF == ord('s'):
            qr = str(qrcode)
            cv2.imwrite('faces\\'+qr+'.png',frame0)
            break
    cv2.destroyAllWindows()
    



###########################################    the end of QRcode


###########################################    app

class OtherFrame(wx.Frame):


    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Secondary Frame")
        panel = wx.Panel(self)
        panel.SetBackgroundColour((153, 0, 153))
        self.im1_n = wx.Image('images\\b_nouveau.png').ConvertToBitmap()
        icon = wx.EmptyIcon()
        icon.CopyFromBitmap(wx.Bitmap("favicon.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)


        msg = "Enter a Message to send to the main frame"
        instructions = wx.StaticText(panel, label=msg)
        self.msgTxt = wx.TextCtrl(panel, value="")
        closeBtn = wx.Button(panel, label="Send and Close")
        closeBtn.Bind(wx.EVT_BUTTON, self.onSendAndClose)

        sizer = wx.BoxSizer(wx.VERTICAL)
        flags = wx.ALL|wx.CENTER
        sizer.Add(instructions, 0, flags, 5)
        sizer.Add(self.msgTxt, 0, flags, 5)
        sizer.Add(closeBtn, 0, flags, 5)
        panel.SetSizer(sizer)


    def onSendAndClose(self, event):
    
        self.Close()



class Nouveau_Frame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, "Nouveau",style= wx.SYSTEM_MENU | wx.CAPTION | wx.MINIMIZE_BOX,size=(400,450),pos=(700, 200))
        panel = wx.Panel(self)


        icon = wx.EmptyIcon()
        icon.CopyFromBitmap(wx.Bitmap("favicon.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)
        panel.SetBackgroundColour((0, 102, 102)) 
        

        wx.StaticText(panel, label="Nouveau Client :",pos=(140, 10))
        
        wx.StaticText(panel, label="Nom :",pos=(20, 50))
        self.nom = wx.TextCtrl(panel, value="",size=(130, 23),pos=(200,50))
        
        wx.StaticText(panel, label="Prenom :",pos=(20, 100))
        self.prenom = wx.TextCtrl(panel, value="",size=(130, 23),pos=(200,100))        
        
        wx.StaticText(panel, label="Tel :",pos=(20, 150))
        self.tel = wx.TextCtrl(panel, value="",size=(130, 23),pos=(200,150))  
        
        wx.StaticText(panel, label="la date :",pos=(20, 200))
        self.choice = wx.Choice(panel,-1,choices = ['1 mois','2 mois','3 mois'],size=(130, 23),pos=(200, 200))
        self.choice.Bind(wx.EVT_CHOICE, self.OnChoice)
        
        new_qr = creat_QRcode()
        GetImage(new_qr)                                      # get and save face image
        wx.StaticText(panel, label="QRcode :",pos=(20, 250))
        self.qrcode = wx.TextCtrl(panel, value=str(new_qr),size=(130, 23),pos=(200,250))        
        
        
        
        nextBtn = wx.Button(panel, label="Ajouter",pos=(70, 340))
        nextBtn.Bind(wx.EVT_BUTTON, self.Next)
        
        closeBtn = wx.Button(panel, label="Close",pos=(210, 340))
        closeBtn.Bind(wx.EVT_BUTTON, self.onClose)
                 
        
        

    def onClose(self, event):
        global QRcode,qre
        QRcode = 10000000
        qre = 10000000
        self.Close()
        
    def Next(self, event): 
        nom = str(self.nom.GetValue())
        prenom = str(self.prenom.GetValue())
        tel = str(self.tel.GetValue())
        date = int((self.date)[0])  #   t = time.localtime(time.time()) mouhim
        date = int(mois2date(date))      #   mois to (datelocale en second + nombra des mois en second
        print(nom,prenom,tel,date)
        qr = creat_QRcode()
        musk_insert(nom,prenom,tel,date,qr,0,0)
        global QRcode
        QRcode = 10000000
        self.Close()
        creat_cart(data = str(qr),nom = nom,prenom = prenom,tel = '0697720846')
        

    def OnChoice(self, event): 
        self.date = self.choice.GetString(self.choice.GetSelection())
          

        
        



class Charger_Frame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Charger",style= wx.SYSTEM_MENU | wx.CAPTION | wx.MINIMIZE_BOX,size=(400,400),pos=(830, 200))
        panel = wx.Panel(self)


        icon = wx.EmptyIcon()
        icon.CopyFromBitmap(wx.Bitmap("favicon.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)
        panel.SetBackgroundColour((0, 102, 102))
        
        
        data = selct_data(qrcode=vrai_qrcode)
        self.qr = data[4]

        wx.StaticText(panel, label="Charger l'abonnement :",pos=(140, 10))
        
        wx.StaticText(panel, label="Nom :",pos=(20, 50))
        self.nom = wx.TextCtrl(panel, value=str(data[0]),size=(130, 23),pos=(200,50))
        
        wx.StaticText(panel, label="Prenom :",pos=(20, 100))
        self.prenom = wx.TextCtrl(panel, value=str(data[1]),size=(130, 23),pos=(200,100))        
        
        wx.StaticText(panel, label="la date :",pos=(20, 150))
        self.choice = wx.Choice(panel,-1,choices = ['1 mois','2 mois','3 mois'],size=(130, 23),pos=(200,150))
        self.choice.Bind(wx.EVT_CHOICE, self.OnChoice)
        
        wx.StaticText(panel, label="QRcode :",pos=(20, 200))
        self.qrcode = wx.TextCtrl(panel, value=str(data[4]),size=(130, 23),pos=(200, 200))        
        
        
        
        closeBtn = wx.Button(panel, label="Next",pos=(70, 290))
        closeBtn.Bind(wx.EVT_BUTTON, self.Next_c)
        
        closeBtn = wx.Button(panel, label="Close",pos=(210, 290))
        closeBtn.Bind(wx.EVT_BUTTON, self.onClose)
        

    def onClose(self, event):
        global Trouve
        global QRcode,qre
        QRcode = 10000000
        qre = 10000000
        self.Close()

        
    def Next_c(self, event): 
        date = int((self.date)[0])
        date = mois2date(date)
        update_date(qrcode=self.qr,date=date)
        global QRcode
        QRcode = 10000000
        self.Close()
    
    def OnChoice(self, event): 
        self.date = self.choice.GetString(self.choice.GetSelection())
        print(self.date)
        
        
        
        
class Information_Frame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Information",style= wx.SYSTEM_MENU | wx.CAPTION | wx.MINIMIZE_BOX,size=(400,400),pos=(960, 200))
        panel = wx.Panel(self)


        icon = wx.EmptyIcon()
        icon.CopyFromBitmap(wx.Bitmap("favicon.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)
        panel.SetBackgroundColour((0, 102, 102))
        
        
        data = selct_data(qrcode=vrai_qrcode)


        wx.StaticText(panel, label="Les informatin de Client :",pos=(120, 10))
        
        wx.StaticText(panel, label="Nom :",pos=(20, 50))
        self.msgTxt = wx.TextCtrl(panel, value=str(data[0]),size=(130, 23),pos=(200,50))
        
        wx.StaticText(panel, label="Prenom :",pos=(20, 100))
        self.msgTxt = wx.TextCtrl(panel, value=str(data[1]),size=(130, 23),pos=(200,100))        
        
        wx.StaticText(panel, label="QRcode :",pos=(20, 150))
        self.msgTxt = wx.TextCtrl(panel, value=str(data[4]),size=(130, 23),pos=(200,150))
        
        wx.StaticText(panel, label="la date :",pos=(20, 200))
        self.msgTxt = wx.TextCtrl(panel, value=str(fin(data[3])),size=(130, 23),pos=(200, 200))        
        

        
        closeBtn = wx.Button(panel, label="Close",pos=(140, 290))
        closeBtn.Bind(wx.EVT_BUTTON, self.onClose)
        

    def onClose(self, event): 
        global QRcode,qre
        QRcode = 10000000
        qre = 10000000
        self.Close()

        

        


#    main frame

class MyPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        
        self.im1 = wx.Image('images\\b_musc1.png').ConvertToBitmap()
        self.im2 = wx.Image('images\\b_musc2.png').ConvertToBitmap()
        self.im3 = wx.Image('images\\b_musc3.png').ConvertToBitmap()
        self.im4 = wx.Image('images\\b_musc4.png').ConvertToBitmap()
        
        self.im5 = wx.Image('images\\b_navbar0.png').ConvertToBitmap()
        self.im6 = wx.Image('images\\b_navbar.png').ConvertToBitmap()
        self.im7 = wx.Image('images\\b_logo.png').ConvertToBitmap()
        
        self.img64 = cv2.imread('images\c1.png')
        self.img65 = cv2.imread('images\c2.png')
        self.img66 = cv2.imread('images\c3.png')
        self.f1 = cv2.imread('images\log.png')
        
        
        img64 = resize_c(self.f1,300,240)
        height, width = img64.shape[:2]
        self.bmp2 = wx.BitmapFromBuffer(width, height, img64)
        self.ImgControl2 = statbmp.GenStaticBitmap(self, wx.ID_ANY, self.bmp2, pos=(880, 130))
        
        img46 = resize_c(frame0,200,200)
        height, width = img46.shape[:2]
        self.orig_height = height
        self.orig_width = width
        self.bmp = wx.BitmapFromBuffer(width, height, img46)
        self.ImgControl = statbmp.GenStaticBitmap(self, wx.ID_ANY, self.bmp, pos=(900, 150))
        
        img64 = resize_c(self.img66,30,100)
        height, width = img64.shape[:2]
        self.orig_height1 = height
        self.orig_width1 = width
        self.bmp1 = wx.BitmapFromBuffer(width, height, img64)
        self.ImgControl1 = statbmp.GenStaticBitmap(self, wx.ID_ANY, self.bmp1, pos=(950, 370))
        

        nouveau = wx.BitmapButton(self,bitmap=self.im1 , size=(120, 80), pos=(10, 10))
        nouveau.Bind(wx.EVT_BUTTON, self.nouveau_def)

        charger = wx.BitmapButton(self,bitmap=self.im2 , size=(120, 80), pos=(140, 10))
        charger.Bind(wx.EVT_BUTTON, self.charger_def)

        information = wx.BitmapButton(self,bitmap=self.im3 , size=(120, 80), pos=(270, 10))
        information.Bind(wx.EVT_BUTTON, self.information_def)
        
#        prix = wx.BitmapButton(self,bitmap=self.im4 , size=(120, 80), pos=(430, 10))
#        prix.Bind(wx.EVT_BUTTON, self.prix_def)
        
        
        
        #start a timer that's handler grabs a new frame and updates the image widgets
        self.timer = wx.Timer(self)
        self.timer.Start(1000.0/25)

        #bind timer events to the handler
        self.Bind(wx.EVT_TIMER, self.NextFrame)
    


    def nouveau_def(self, event):
        frame = Nouveau_Frame()
        frame.Show()

    def charger_def(self, event):
        global vrai_qrcode
        vrai_qrcode = lire_qrcode()
        if not(vrai_qrcode==False) :
            frame = Charger_Frame()
            frame.Show()
        
    def information_def(self, event):
        global vrai_qrcode
        vrai_qrcode = lire_qrcode()
        if not(vrai_qrcode==False) :
            frame = Information_Frame()
            frame.Show()

#    def prix_def(self, event):
#        of = 0
##        self.dc.DrawBitmap(self.im5, 100, 100, True)
##        frame = OtherFrame()
##        frame.Show()
        
    def OnPaint(self, evt):
        self.dc = wx.PaintDC(self)

        self.dc.DrawBitmap(self.im5, 0, 0, True)
        self.dc.DrawBitmap(self.im6, 0, 100, True)
        self.dc.DrawBitmap(self.im7, 1050, 10, True)
        
#        self.dc.DrawRectangle(440,480,310,270)
#        self.dc.DrawRoundedRectangle(440,480,310,270,100)
#        self.dc.DrawCheckMark(100,200,20,20)
        
    def NextFrame(self, event):
        global Trouve
        qr = QRcode
        
        if Trouve==True:
            t_db = selct_time(qrcode=qr)
            t_moin = t_db-time.time()
            if t_moin>0:
                
                mixer.init()
                mixer.music.load('audio/vrai.mp3')
                mixer.music.play()
                
                frame1 = cv2.imread('faces\\'+str(qr)+'.png')
                img46 = resize_c(frame1,200,200)
                img46 = cv2.cvtColor(img46, cv2.COLOR_BGR2RGB)
                self.bmp.CopyFromBuffer(img46)
                self.ImgControl.SetBitmap(self.bmp)
                
                
                img64 = resize_c(self.img65,30,100)
                img64 = cv2.cvtColor(img64, cv2.COLOR_BGR2RGB)
                self.bmp1.CopyFromBuffer(img64)
                self.ImgControl1.SetBitmap(self.bmp1)
                
            else:
                
                mixer.init()
                mixer.music.load('audio/false.mp3')
                mixer.music.play()
                
                frame1 = cv2.imread('faces\\'+str(qr)+'.png')
                img46 = resize_c(frame1,200,200)
                img46 = cv2.cvtColor(img46, cv2.COLOR_BGR2RGB)
                self.bmp.CopyFromBuffer(img46)
                self.ImgControl.SetBitmap(self.bmp)
                
                
                img64 = resize_c(self.img65,30,100)
                img64 = cv2.cvtColor(img64, cv2.COLOR_BGR2RGB)
                self.bmp1.CopyFromBuffer(img64)
                self.ImgControl1.SetBitmap(self.bmp1)
        
            Trouve=False
        

        
        

class MyFrame(wx.Frame):



    def __init__(self):

        wx.Frame.__init__(self, None, title="B.musculation",style= wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX,size=(1200,800),pos=(600, 100))
        panel = MyPanel(self)
        icon = wx.EmptyIcon()
        icon.CopyFromBitmap(wx.Bitmap("favicon.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)
        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
    del app

stop = True
cv2.destroyAllWindows()

###########################################    the end of app





