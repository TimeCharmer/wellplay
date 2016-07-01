#-*-encoding=utf-8-*-
'''
Created on 2016年6月28日
quick sort test
data=random.sample(range(100),10)
quicksort(data,0,len(data)-1)
@author: Administrator
'''
import random

def quicksort(arr,p,r):
    if p<r:
        q=partition(arr,p,r)
        quicksort(arr, p, q-1)
        quicksort(arr, q+1, r)
        
def partition(arr,p,r):
    x=arr[r]
    i=p-1
    for j in range(p,r):
        if arr[j]<=x:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1

if __name__=='__main__':
    data=random.sample(range(100),10)
    print 'original data',data
    quicksort(data,0,len(data)-1)
    print 'sorted data',data
    