#Problem Code:
#SLICE1_PY

t=int(input())
while(t):
    l=int(input())
    
    arr = [int(x) for x in input().split()]
    arr.reverse()
    for i in range(0,l):
        print(arr[i],end=" ")
    print("")    
    arr.reverse()
    for i in range(0,l):
        if i>=3:
            if i%3==0:
                print(arr[i]+3,end=" ")
    print("")  
    for i in range(0,l):
        if i>=5:
            if i%5==0:
                print(arr[i]-7,end=" ")
    print("")  
    sum=0
    for i in range(3,8):
        sum=sum+arr[i]
    print(sum)    
    
    t=t-1 