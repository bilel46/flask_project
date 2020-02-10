import sqlite3
import json
import numpy as np
import cv2


def create_db(name='musculation.db'):
    conn = sqlite3.connect(name)
    conn.commit()
    conn.close()


def create_table(database_name='musculation.db',table_name='client',col=['nom text','prenom text','tel text','date integer','qrcode integer','many integer','id integer']):
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
    insert_data(col_data=['bilel text','boumediene text','0697720832 text','1577020979 integer','10000000 integer','0 integer','0 integer'])
    
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

def clients(database_name='musculation.db',table_name='client',id='0'):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()    
    c.execute("SELECT * FROM {} WHERE id={}".format(table_name,id))
    p = c.fetchall() 
    return p

    
create_db()
create_table()

insert_data(col_data=['walid text','boumediene text','0697720832 text','1111 integer','10000001 integer','0 integer','0 integer'])
insert_data(col_data=['aymen text','lwati text','0697725898 text','1574520979 integer','10000002 integer','0 integer','0 integer'])
insert_data(col_data=['hawari text','boumediene text','0697754832 text','0 integer','10000003 integer','0 integer','0 integer'])
insert_data(col_data=['miloude text','siki text','0697257832 text','1577250979 integer','10000004 integer','0 integer','0 integer'])

update_date(database_name='musculation.db',table_name='client',qrcode=24685795,date=100000)
update_many(database_name='musculation.db',table_name='client',qrcode=24685795,many=1500)

def musk_insert(nom,prenom,tel,date,qrcode,many,idi):
    insert_data(col_data=[nom+' text',prenom+' text',tel+' text',str(date)+' integer',str(qrcode)+' integer',str(many)+' integer',str(idi)+' integer'])

a = 'nnn'
b = 'nnnjjj'
c = '0697720813'
d = 1990
e = 10000010
f = 500
g = 0


musk_insert(a,b,c,d,e,f,g)

p = selct_data(qrcode=10000010)
print(p)




qr = creat_QRcode()
print(qr)



























