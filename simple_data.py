#-*-encoding=utf-8-*-
'''
Created on 2016年7月8日

@author:whr
'''
import sys,shelve
def store():
    s=shelve.open('test.dat')
    # s['x']=['a','b','c']
    s['x']=['狗','头','人','陈','旭']
    for i in range(len(s['x'])):
         print s['x'][i],
    s.close()
if __name__=='__main__':
    store()