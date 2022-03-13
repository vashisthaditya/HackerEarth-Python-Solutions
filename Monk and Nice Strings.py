value=int(input())
arr=[]
for i in range(value):
    arr.append(input())
 
 
 
for j in range(value):
    count=0
    for k in range(j):
        if arr[k]<arr[j]:
            count+=1
            
    print(count)