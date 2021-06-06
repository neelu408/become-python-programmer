def findmin(n,data):
    s=data[0]
    l=data[0]
    c=0
    for i in range(1,n):
           if s>data[i]:    
               s=data[i]
               c=c+1
               p=i
               
               
    return s,c,p
n=int(input())
data=list(map(int,input().split()))
minval=findmin(n,data)
print(*minval)

            
        
    
