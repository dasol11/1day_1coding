def solution(arr):
    stk = []
    i = 0
    while i != len(arr):
        if stk:
            if stk[-1] == arr[i]:
                stk.pop()
            else:
                stk.append(arr[i])
        else:
            stk.append(arr[i])
        
        i += 1
    return stk or [-1]



def solution(arr):
    stk = []
    for i in range(len(arr)):
        if stk and stk[-1] == arr[i]:
            stk.pop()
        else:
            stk.append(arr[i])

    return stk or [-1]    

a = solution([0, 1, 1, 1, 0])
print(a)