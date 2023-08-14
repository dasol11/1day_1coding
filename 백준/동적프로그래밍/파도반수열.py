import sys

input = sys.stdin.readline
T = int(input())




# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16
for _ in range(T):
    N = int(input())
    arr = [0]*101
    arr[0],arr[1],arr[2] = 1,1,1
    for i in range(3,N):
        arr[i] = arr[i-3] + arr[i-2]
        
    print(arr[N-1])
