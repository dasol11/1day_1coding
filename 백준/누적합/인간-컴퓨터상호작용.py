import sys
input = sys.stdin.readline

w = input()

N = int(input())

for i in range(N):
    a = list(map(str, input().split()))
    
    answer = 0
    for j in range(int(a[1]),int(a[2])+1):
        if w[j] == a[0]:
            answer +=1
    print(answer)
    
    
    