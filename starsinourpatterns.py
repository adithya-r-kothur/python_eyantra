#Problem Code:
#STAR_PY


t=int(input())
while(t):
    n=int(input())
    flag=0
    for i in range(n,0,-1):
        for j in range(0,i):
            if flag==4:
                print("#",end="")
                flag=0
            else:    
                print("*",end="")
                flag=flag+1
        flag=0        
        print("")
    t=t-1