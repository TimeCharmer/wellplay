#-*-encoding=utf-8-*-
'''
Created on 2016年7月1日
test the random module 
python3.3的random模块实现各种分布下的伪随机数生成。
对整数而言，可以在一个范围内按均匀分布来随机选择。对序列来说，同样可以按照均匀分布来选择一个元素，可以对数组产生随机排列，也可以进行随机的不重复采样。

对随机实数而言，提供均匀，正态（高斯），对数正态，负指数，γ和β等多种分布。甚至角分布和冯·米塞斯分布（循环正态分布），
@author: Administrator
'''
import random

def testRandom():
    #在[a,b]之间产生随机整数
    for i in range(5):
        ret=random.randint(100,999)
        print ("random.randint(100,999)={0}".format(ret,))

if __name__=='__main__':
    testRandom()