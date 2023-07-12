import sys
input = sys.stdin.readline

primeNum = [False, False] + [True]*999999

for i in range(2, 1000001):
    if primeNum[i]:
        for j in range(i*2, 1000001, i):
            primeNum[j] = False

T = int(input())

for _ in range(T):
    answer = 0
    N = int(input())
    
    for i in range(2, N//2 +1):
        if primeNum[i] and primeNum[N-i]:
            answer += 1
            
    print(answer)