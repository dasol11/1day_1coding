def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        stack = []
        for i in arr[s:e+1]:
            if k < i:
                stack.append(i)
        
        if stack == []:
            answer.append(-1)
        else:
            answer.append(min(stack))
    return answer

a = solution([0, 1, 2, 4, 3],[[0, 4, 2],[0, 3, 2],[0, 2, 2]])
print(a)