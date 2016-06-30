#-*-encoding=utf-8-*-
'''
Created on 2016年6月27日

@author: Administrator
N quees problem solution show 
'''
import sys,random
def conflict(state,nextX):
    '''
    detect for the conflict of queens
    '''
    nextY=len(state)
    for i in range(nextY):
       if abs(state[i]-nextX) in (0,nextY-i):
           return True
    return False 

def quees(num=8,state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state)==num-1:
                yield (pos,)
            else:
                for result in quees(num, state+(pos,)):
                    yield(pos,)+result

#打印结果
def prettyprint(solution):
    def line(pos,lenth=len(solution)):
        return '. '*(pos)+'X '+'. '*(lenth-pos-1)
    for pos in solution:
        print line(pos)
        
if __name__=='__main__':
    prettyprint(random.choice(list(quees(8))))