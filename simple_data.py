#-*-encoding=utf-8-*-
'''
Created on 2016年7月8日

@author:whr
'''
import sys,shelve
def store():
    s=shelve.open('test.dat')
    s['x']=['a','b','c']
    print s['x']
    s.close()
if __name__=='__main__':
    store()