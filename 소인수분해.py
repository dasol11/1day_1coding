def solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            answer.append(d)
            n = n / d
        else:
            d += 1
    return sorted(answer)



a = solution(420)
print(a)