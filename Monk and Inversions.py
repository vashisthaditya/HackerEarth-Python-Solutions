value1=int(input())
for i in range(value1):
    rows=int(input())
    my_list = []
    for j in range(rows):
        my_list.append(list(map(int, input().split())))
     
    count=0
    for k in range(rows):
        for m in range(rows):
            for x in range(k,rows):
                for y in range(m,rows):
                    if(my_list[x][y]<my_list[k][m]):
                        count+=1
                    else:
                        continue    
    print(count)