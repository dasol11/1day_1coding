def gcd(a,b):
    
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def factorization(x):
    d = 2
    stk = []
    while d <= x:
        if x % d == 0:
            stk.append(d)
            x /= d
        else:
            d += 1
    return stk


def solution(a, b):
    gcd_num =  gcd(a,b)
    a /= gcd_num
    b /= gcd_num
    
    stk = factorization(b)
    while 2 in stk:
        stk.remove(2)
        
    while 5 in stk:
        stk.remove(5)

    if stk:
        return 2
    else:
        return 1

c = solution(7,20)
print(c)