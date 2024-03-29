import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * N

arr = [int(input()) for _ in range(N)]
dp[0] = arr[0]

if N > 1:
    dp[1] =  arr[0]+ arr[1]
    
if N > 2:
    dp[2] = max(arr[2]+arr[1],arr[2]+arr[0],dp[1])
for i in range(3, N):
    dp[i] = max(dp[i-1],dp[i-3]+arr[i-1]+ arr[i], dp[i-2]+arr[i])


print(dp[N-1])
print(dp)
