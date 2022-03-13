from collections import Counter
test_case=int(input())
for i in range(test_case):
    N=int(input())
    arr=list(map(int,input().split()))
    my_dict = dict(Counter(arr))           
      
    keys=[]
    values=[]
    items=my_dict.items()
    for j in items:
        keys.append(j[0]), values.append(j[1])
    
    max_number_count=max(values)    
    min_number_value=min(values)
    answer=max_number_count-min_number_value
 
    if(answer>0):
        print(answer)
    else:
        print("-1")