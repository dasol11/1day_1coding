def solution(polynomial):
    skt = polynomial.split(" + ")
    x = 0
    n = 0 
    for i in skt:
        if i.isdigit():
            n += int(i)
        else:
            if len(i) ==1:
                x +=1
            else:
                x += int(i[:-1])
    if x == 0:
        return str(n)
    elif x == 1:
        return "x + "+str(n) if n !=0 else "x"
    else:
        return str(x)+"x + "+str(n) if n !=0 else str(x)+"x"

a= solution("1")
print(a)