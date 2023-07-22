import sys

input = sys.stdin.readline


def star(arr, s, N):
    temp = N // 3
    if temp == 0:
        return
    for i in range(s[0] + temp, s[0] + 2*temp):
        for j in range(s[1] + temp, s[1] + 2*temp):
            arr[i][j] = " "
            
    for k in range(s[0], s[0]+N, temp):
        for l in range(s[1], s[1]+N, temp):
            star(arr ,[k,l], temp)
    
    
N = int(input())

arr = [["*" for _ in range(N)] for _ in range(N)]


star(arr, [0,0], N)

for i in arr:
    print("".join(i))
