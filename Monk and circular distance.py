from math import sqrt
from bisect import bisect_left
from bisect import bisect_right
 
 
n=int(input())
arr=[]
for i in range(n):
    element=list(map(int,input().split()))
    arr.append(element)
 
sqrt_arr=[]
for i in range(n):
    d=sqrt(arr[i][0]**2+arr[i][1]**2)
    sqrt_arr.append(d)
 
sqrt_arr.sort()
 
q=int(input())
for j in range(q):
    element2=int(input())
    count=bisect_right(sqrt_arr,element2)
    print(count)