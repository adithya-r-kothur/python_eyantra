#Problem Code:
#WLEN_PY

t=int(input())
while(t):
    p=input()
    x=p.split()
    a=len(x)
    y=[None] * a
    
    for i in range(0,a):
        if i==0:
            print(len(x[i])-1,end=",")
        else:    
            print(len(x[i]),end="")
            if i!=a-1:
                print(end=",")
        
    print("")
    t=t-1