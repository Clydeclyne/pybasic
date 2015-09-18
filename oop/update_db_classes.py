# -*-coding:utf-8 -*-
__author__ = 'Clyde Ding'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import shelve
db = shelve.open('class-shelve')
sue = db['sue']
sue.giveRaise(.25)
db['sue'] = sue
tom = db['tom']
tom.giveRaise(.20)
db['tom'] = tom
db.close()