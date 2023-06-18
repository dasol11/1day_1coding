def solution(arr):
    li = []
    for idx, val in enumerate(arr):
        if val == 2 :
            li.append(idx)
    if li :
        s = min(li)
        e = max(li)+1
        return arr[s:e]
    else:
        return [-1]
a = solution([1, 2, 1, 4, 5, 2, 9])
print(a)

b = solution([1, 2, 1])
print(b)

c = solution([1, 1, 1])
print(c)
