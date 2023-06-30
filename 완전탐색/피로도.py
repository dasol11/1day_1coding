def solution(k, dungeons):
    answer = 0
    for m, n in enumerate(dungeons):
        while k >= m :
            k -= n
            answer += 1
    return answer


a = solution([[80,20],[50,40],[30,10]])


# k = 40
# [[40, 20], [10, 10], [10, 10], [10, 10], [10, 10]]
# answer = 4