def p(N):
    if N <= 1:
        return N
    return p(N-1)+ p(N-2)

print(p(10))