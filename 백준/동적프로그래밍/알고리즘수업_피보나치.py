import sys


def fin (n):
    if n ==1 or n ==2:
        return 1
    else:
        return fin(n-1) + fin(n-2)
    
def finbonacci(n):
    stk = [0]* (n+1)
    cou_fin = 0
    stk[1],stk[2] = 1,1
    for i in range(3, n+1):
        stk[i] = stk[i-1]+stk[i-2]
        cou_fin += 1
    return cou_fin

n = int(input())

print(fin(n),  finbonacci(n))
