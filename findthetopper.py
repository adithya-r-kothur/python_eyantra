#Problem Code:
#SCOR_PY


from collections import OrderedDict
def Convert(string):
	li = list(string.split(" "))
	return li
def add_value(dict_obj, key, value):
    
    if key not in dict_obj:
        dict_obj[key] = value
    elif isinstance(dict_obj[key], list):
        dict_obj[key].append(value)
    else:
        dict_obj[key] = [dict_obj[key], value]
        
t=int(input())
while(t):
    n=int(input())
    ab=[None]*100
    student = {}

    for x in range(n):    
        new_key,new_age = input().split()
        add_value(student, new_age, new_key)
    dict1 = OrderedDict(sorted(student.items())) 
    
    ab=list(dict1.values())[-1]
    if isinstance(ab, str):
        size=0
        st=Convert(ab)
        for i in st:
            size+=1
        if size>1:
            st.sort()
    
        for i in range(0,size):
            print(st[i],end=" ")
    else:
        size=0
        for i in ab:
            size+=1
        if size>1:
            ab.sort()
        for i in range(0,size):
            print(ab[i])
    
    t=t-1