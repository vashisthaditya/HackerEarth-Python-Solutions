test_cases=int(input())
for i in range(test_cases):
    size_of_arr=int(input())
    arr=list(map(int,input().split()))
    arr_length=len(arr)
 
    arr.sort()
    new_arr=[]
 
    for j in range(arr_length-1):
        x=(arr[j] and arr[j+1])^(arr[j] or arr[j+1])
        new_arr.append(x)
    
    print(min(new_arr))