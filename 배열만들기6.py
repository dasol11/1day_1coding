def solution(arr):
    stk = []
    i = 0
    while i != len(arr):
        if stk:
            if stk[-1] == arr[i]:
                stk[-1] += 1
            else:
                stk.insert(0, arr[i])
        else:
            stk.append(arr[i])
        print(stk)
        i += 1
    return stk


a = solution([0, 1, 1, 1, 0])
print(a)