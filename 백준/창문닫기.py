import sys
# N = int(sys.stdin.readline())

# dic = {i:0 for i in range(1,N+1)}


# for j in range(1,N+1):
#     for k in range(1, N+1):
#         if k % j == 0 :
#            if dic[k] == 1:
#                dic[k] = 0
#            else:
#                dic[k] = 1

# print(sum([i for i in dic.values()]))

# 위 코드로 제출시 메모리 초과

# 1, 4, 9, 25  순으로 +1 씩 증가함 
print(int(float(input())**0.5))