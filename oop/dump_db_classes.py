# -*-coding:utf-8 -*-
__author__ = 'Clyde Ding'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import shelve
db = shelve.open('class-shelve')
for key in db:
    print(key, '=>\n ', db[key].name, db[key].pay)
bob = db['bob']
print(bob.lastName())
print(db['tom'].lastName())