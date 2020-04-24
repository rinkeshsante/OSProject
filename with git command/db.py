import sqlite3

class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute('create table if not exists parts(id INTEGER PRIMARY KEY,name text,idNo INTEGER,price INTEGER,quantity INTEGER)')
        self.conn.commit()
    
    def fetch(self):
        self.cur.execute('select * from parts')
        rows = self.cur.fetchall()
        return rows
    
    def insert(self,name,idNo,price,qnt):
        self.cur.execute('insert into parts values(NULL,?,?,?,?)',(name,idNo,price,qnt))
        self.conn.commit()
    
    def remove(self,id):
        self.cur.execute('delete from parts where id=?',(id,))
        self.conn.commit()

    def update(self,id,idNo,name,price,qnt):
        self.cur.execute('update parts set name=?,idNo=?,price=?,quantity=? where id =?',(name,idNo,price,qnt,id))
        self.conn.commit()
    
    def __de__(self):
        self.conn.close()

'''
db=Database('store.db')
db.insert('firts','33','45','355')
db.insert('second','33','45','355')
'''

import subprocess
import os

class Database1:
    def __init__(self):
        pass


    def cmd_call(self,cmd):
        """
        runs any git command then returns its output and error
        :param cmd: string
        :return: out: string, err: string
        """
        test = subprocess.Popen(['ls',], stdout=subprocess.PIPE)
        output = test.communicate()[0]
        return output
        

db = Database1()


print('--------------------',db.cmd_call('sqlite3 test.db'))



