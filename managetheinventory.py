#Problem Code:
#INV_PY




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
    items={}
    for i in range(0,n):
        name,quantity = input().split()
        add_value(items, name, int(quantity))
    
    m=int(input())
    while(m):
        op,item,qua=input().split()
        if op=="ADD":
            if item in items:
                items[item]=items[item]+int(qua)
                print(f"UPDATED Item {item}")
            else:
                items[item]=int(qua)
                print(f"ADDED Item {item}")
        else:
            if item in items:
                if items[item]<int(qua):
                    print(f"Item {item} could not be DELETED")
                else:
                    items[item]=items[item]-int(qua)
                    print(f"DELETED Item {item}")
            else:
                print(f"Item {item} does not exist")
            
        m=m-1
        sum=0
    for i in items.values():
        sum+=i
    print(f"Total Items in Inventory: {sum}")
    t=t-1