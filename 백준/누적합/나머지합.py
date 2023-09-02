import sys
input = sys.stdin.readline

N, M = map(int,input().split())


arr = list(map(int,input().split()))

dp = [0] * M
s = 0

for i in range(N):
    s += arr[i]
    dp[s%M] += 1

answer = dp[0]

for i in dp:
    answer += i*(i-1)//2
print(answer)

# 내 코드 시간초과

# dp = [0] * (N+1)
# for i in range(1,N+1):
#     dp[i] = dp[i-1] + arr[i-1]

# answer = 0

# for j in range(N+1):
#     for k in range(j):
#         if (dp[j]-dp[k]) % M == 0:
#             answer += 1

# print(answer)


