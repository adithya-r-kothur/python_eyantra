#Problem Code:
#APLAM1_PY


import functools
from functools import reduce

import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())


def generate_AP(a1, d, n):

    AP_series = [0] * (n)

    
    AP_series[0]=a1
    for i in range(2,n+1):
         AP_series[i-1] =a1+(i-1)*d
        

    return AP_series



if __name__ == '__main__':
    
   
    t = int(input())

    
    while(t):
        a1,d,n = get_ints()
    

        
        AP_series = generate_AP(a1, d, n)
        for i in range(0,n):
            print(AP_series[i],end=" ")
        print("")
       
        sqr_AP_series = list(map(lambda x: x ** 2, AP_series))
        for i in range(0,n):
            print(sqr_AP_series[i],end=" ")
        print("")
        sum_sqr_AP_series = functools.reduce(lambda a, b: a+b, sqr_AP_series)    
        print(sum_sqr_AP_series)
        t=t-1