import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))

dp = [0] *(N-M+1)
dp[0] = sum(arr[:M])
for i in range(1, N-M+1):
    dp[i] = dp[i-1]-arr[i-1]+arr[i+M-1]

    print(dp)
print(max(dp))
    