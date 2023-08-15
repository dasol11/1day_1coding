import sys
input = sys.stdin.readline


N = int(input())

dp = [[0,0,0] for _ in range(N)]
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
    
    if i == 0:
        dp[0][0],dp[0][1],dp[0][2] = arr[0][0], arr[0][1], arr[0][2]
        
    else:
        dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + arr[i][0]
        dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + arr[i][1]
        dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + arr[i][2]        
print(min(dp[N-1]))
