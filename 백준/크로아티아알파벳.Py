a = input()
stk = ["c=", "c-", "dz=", "d-", "lj", "nj","s=", "z="]
for i in stk:
    a = a.replace(i,"*") 
    print(a)      
print (len(a))
