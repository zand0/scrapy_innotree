# -*- coding: utf-8 -*-
import sqlite3
import sys
sys.path.append('..')
from confs.conf import conf

class Sqlite3Helper():
    cx=''
    cu=''
    def __init__(self):
        self.cx = sqlite3.connect(conf['sqlitedb']['dbname'])
        self.cu=self.cx.cursor()
    
    def fetch(self,sql,statement=None):
        if statement==None:
            self.cu.execute(sql)
        return self.cu.fetchone()

    def fetchall(self,sql,statement=None):
        if statement==None:
            self.cu.execute(sql)
        return self.cu.fetchall()

    def execute(self,sql,statement=None):
        if statement==None:
            self.cu.execute(sql)
            self.cx.commit()
        else:
            self.cu.execute(sql,statement)
            self.cx.commit()
    def __del__(self):
        self.cx.close()