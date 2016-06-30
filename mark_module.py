#-*-encoding=utf8-*-
'''
Created on 2016年6月28日

@author: Administrator
'''
#输出比下面哪种多了个空格
while True:
    try:
        number=input()
        i=2
        while number!=1:
            while number%i==0:
                print i,
                number/=i
            i+=1
        #print "",
    except:
        break
# import sys
#   
# while True:
#     try:
#         number = long(sys.stdin.readline())
#         i = 2
#   
#         while number != 1:
#             while number % i == 0:
#                 print i,
#                 number = number / i
#             i = i + 1
#         print "",
#     except:
#         break
         

