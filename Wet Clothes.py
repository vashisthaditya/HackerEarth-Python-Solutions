n,m,g= map(int,input().split())
arr_rain=list(map(int,input().split()))
arr_dry=list(map(int,input().split()))
 
arr_diff=[]
count=0
for i in range(n-1):
        x=arr_rain[i+1]-arr_rain[i]
        arr_diff.append(x)
        x=max(arr_diff)
 
for j in range(m):
        if arr_dry[j]<=x:
                count+=1
 
    
 
print(count)