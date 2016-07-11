#!/usr/bin/env python
#-*-encoding=utf-8-*-                   # 1
'''                                     # 2
Created on 2016年7月11日             # 3
为Python脚本添加行号             # 4
因为汉字的存在对不齐了，想想怎么办
@author: {weihaoran}                    # 5
'''                                     # 6
import fileinput                        # 7
for line in fileinput.input(inplace=0): # 8
    line=line.rstrip()                  # 9
    num=fileinput.lineno()              #10
    print '%-40s#%2i'%(line,num),'len:',len(line)        #11
fileinput.close()                       #12
