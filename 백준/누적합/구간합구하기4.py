import sys
input = sys.stdin.readline


N, M = map(int, input().split())

arr = list(map(int, input().split()))
dp = [0] * (N+1)

dp[1] = arr[1]

for x in range(1,N+1):
    dp[x] = dp[x-1] + arr[x-1]
print(dp)
for _ in range(M):
    i, j = map(int, input().split())
    
    print(dp[j]-dp[i-1])


# for _ in range(M):
    
#     i, j = map(int, input().split())
    
#     print(sum(arr[(i-1):(j)]))