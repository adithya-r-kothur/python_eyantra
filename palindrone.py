#Problem Code:
#PAL_PY

t=int(input())
while(t):
  s=str(input())
  a=0
  for i in range(int(len(s)/2)):
      if ord(s[i])==ord(s[len(s)-i-1]):
        a=a+1
      elif ord(s[i])==ord(s[len(s)-i-1])+32 :
        a=a+1
      elif ord(s[i])+32==ord(s[len(s)-i-1]):
       a=a+1
    
    
    
       
  if a==int(len(s)/2):
   print("It is a palindrome\n")
   t=t-1
  else:
   print("It is not a palindrome\n")
   t=t-1