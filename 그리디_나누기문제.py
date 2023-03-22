

def sol (N, K):
    count = 0
    while N !=1 :
            
        if N % K == 0:
            N = N/K
        else:
            N -= 1
        count += 1
        
    return count    


def sol2 (N, K):
    count = 0
    
    while True:
        target = (N//K) * K
        count += (N-target)
        N = target
        if N < K:
            break
        count +=1
        N //= K
    count += (N-1)
    return count
a = sol(25, 3)
print(a)

b = sol(25, 5)
print(b)

c = sol2(25, 3)
print(c)

d = sol2(25, 5)
print(d)

