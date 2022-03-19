from bisect import bisect_left
from bisect import bisect_right
n=int(input())
 
arr=list(map(int,input().split()))
q=int(input())
 
 
 
arr.sort()
 
for i in range(q):
        a,b=map(int,input().split())
        if a==0:
                count=len(arr)-bisect_left(arr,b)
        else:
                count=len(arr)-bisect_right(arr,b)
        print(count)