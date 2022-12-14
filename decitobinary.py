#Problem Code:
#D2BIN1_PY

def decimalToBinary(n):
    bin = 0
    ctr = 0
    tem = n
    while(tem > 0):
        bin = ((tem%2)*(10**ctr)) + bin
        tem = int(tem/2)
        ctr += 1
  
    return bin

if __name__ == '__main__':
    t=int(input())
    while(t):
        n=int(input())
        bin=decimalToBinary(n)
        print(f"{bin:08d}")
        t=t-1 