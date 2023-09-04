import sys
input = sys.stdin.readline


N = int(input())
dp = [1] * N

arr = [list(map(int,input().split())) for _ in range(N)]

arr.sort()
print(arr)
for i in range(1, N):
    for j in range(0,i):
        if arr[j][1] < arr[i][1]:
            dp[i] = max(dp[i], dp[j]+1)
            
print(N-max(dp)) 