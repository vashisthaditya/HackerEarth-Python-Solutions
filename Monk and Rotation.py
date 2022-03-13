from collections import deque
value1=int(input())
for i in range(value1):
    
    value2=input()
    value3=input()
    
    value5=value2.split()
    value4=value3.split()
    
    value6=int(value5[1])
    
    value4=deque(value4)
    value4.rotate(value6)
    value4= list(value4)
    
    glue=' '
    value4=glue.join(value4)
 
    print(value4)