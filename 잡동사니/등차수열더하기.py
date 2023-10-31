def solution(a, d, included):
    answer = 0
    s = a
    for i in range(len(included)):
        s += d
        if included[i] == True:
            answer += s
        print(s)
    return answer


a = solution(3,	4,[True, False, False, True, True])

print(a)