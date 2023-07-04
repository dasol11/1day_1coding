while True:
    stk =[]
    n = int(input())
    s = 0
    if n == -1:
        break
    for i in range(1,n):
        if n% i ==0 :
            stk.append(str(i))
            s += i
    
    if n == s:
        print(str(n)+" = " + " + ".join(stk))
    else:
        print(str(n)+" is NOT perfect.")
    