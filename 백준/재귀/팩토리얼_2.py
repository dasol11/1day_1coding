import sys
input = sys.stdin.readline
def factorial_rec (N):
    if N <= 1:
        return 1
    return N * factorial_rec(N-1)
N = int(input())
print(factorial_rec(N))
    