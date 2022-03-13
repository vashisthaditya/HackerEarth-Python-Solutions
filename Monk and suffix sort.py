str1,int1=input().split()
 
arr=[]
for i in range(len(str1)):
    str2=str1[i:len(str1)]
    arr.append(str2)
 
 
int2=int(int1)
arr.sort()
print(arr[int2-1])