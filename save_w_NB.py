import numpy as np


def w_creat_data_base(data_base_name):
    import sqlite3                                      
    conn = sqlite3.connect(data_base_name)
    c = conn.cursor()
    c.execute('''
              CREATE TABLE wt
              (id INTEGER PRIMARY KEY, array BLOB)
              ''')
    conn.commit()
    conn.close()
    
def save_data_in_data_base(data_base_name,w):
    import sqlite3
    import json
    conn = sqlite3.connect(data_base_name)
    with conn:
        c = conn.cursor()
        c.execute('SELECT * FROM wt')
        for i in range(len(w)):
            c.execute("INSERT INTO wt VALUES (?,?)", (i,json.dumps(w[i].tolist())))
    conn.close()
    
def select_data_in_data_base(data_base_name,NB_hiden_layers):
    import sqlite3
    import json
    conn = sqlite3.connect(data_base_name)
    w = []
    with conn:
        c = conn.cursor()
        c.execute("SELECT * FROM wt")
        y = c.fetchall()
        for i in range(NB_hiden_layers+1):
            w.append(np.array(json.loads((y[i])[1])))
    conn.close()
    return w













    