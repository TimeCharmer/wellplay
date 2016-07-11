#-*-encoding=utf-8-*-
'''
Created on 2016年7月11日
斐波拉契数列的黄金比例倒数（√5+1）/2
@author: {weihaoran}
'''
def fibmethod(n):
    a=0
    b=1
    for i in range(n):
        a,b=b,a+b
    return b
print (5**0.5-1)/2
print fibmethod(99)*1.0/fibmethod(100)
