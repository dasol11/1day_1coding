def solution(sides):
    answer = 0
    n = min(sides)
    m = max(sides)
    for i in range(m+1):
        if (i + n ) > m:
            answer +=1
            print(i, answer)
    for i in range(m+1,n+m):
        if (n+m) > i:
            answer +=1
            print(i, answer)
    return answer

a= solution([3, 6])