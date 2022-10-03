#Problem Code:
#IFFOR1_PY

t=int(input())
while(t):
 n=int(input())
 for i in range(0,n):
   if i==0:
     print(i+3,end=" ")
   else:
     if i%2==0: 
       print(i*2,end=" ")
     else:
       print(i*i,end=" ")
 t=t-1        
 print("") 