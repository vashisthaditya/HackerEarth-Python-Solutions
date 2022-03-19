N=int(input())
arr=list(map(int,input().split()))
#arr=list(map(int,input().strip().split(" ")))
max_arr=max(arr)
 
i=1
j=10**5
while max_arr:
    arr.sort(key=lambda x: (x/i)%j)
 
    print(' '.join(map(str,arr)))
    i*=j
    max_arr//=j