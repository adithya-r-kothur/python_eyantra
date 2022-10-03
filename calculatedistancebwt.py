#Problem Code:
#DIST1_PY

t=int(input())
while(t):
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    
    dis=((x1 - x2)**2 + (y1 - y2)**2)**0.5
    format_float = "{:.2f}".format(dis)
    print("Distance:",format_float)
   
  
    t=t-1