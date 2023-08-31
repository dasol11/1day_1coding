import sys
input = sys.stdin.readline



N = int(input())

arr = list(map(int,input().split()))
rev_arr = arr[::-1]
dp = [1] * N
rev_dp = [1] * N
for i in range(N):
    for j in range(i):
        
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)
        if rev_arr[j] < rev_arr[i]:
            rev_dp[i] = max(rev_dp[i], rev_dp[j]+1)
            
result = [0] *  N

for k in range(N):
    result[k] = dp[k] + rev_dp[N-k-1] - 1
   
print(max(result))
