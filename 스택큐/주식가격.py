
# # 내 코트 완전탐색에  가까운 코드
# def solution(prices):
#     stk = [[t, p] for t, p in enumerate(prices)]
#     save =[]
    
#     while  stk:
#         s = stk.pop(0)
#         for t, p in stk:
#             if s[1] > p:
#                 break
#         s[0] = t -s[0]
#         save.append(s)
#     return [i[0] for i in save]

# def solution(prices):
#     stk = [0 for _ in range(len(prices))]
    
#     for i in range(len(prices)):
#         for j in range(i+1 ,len(prices)):
#             if prices[i] <= prices[j]:
#                 stk[i] += 1
#             else:
#                 stk[i] += 1
#                 break
                
#     return stk



def solution(prices):
    answer = [0]*len(prices)
    stk = []
 
    for t, p in enumerate(prices):
        #stack이 비었이면 false
        print(t, p, stk)
        while stk and p < prices[stk[-1]]:
            j = stk.pop()
            answer[j] = t - j
        stk.append(t)
    print(t, p, stk)
    # for문 다 돌고 Stack에 남아있는 값들 pop
    while stk:
        j = stk.pop()
        answer[j] = len(prices) - 1 - j
 
    return answer

a = solution([1, 2, 3, 2, 3])
print(a)