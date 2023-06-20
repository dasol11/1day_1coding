def solution(s):
    answer = 0
    lat_num = 0
    stk = s.split()
    for i in stk:
        print(i)
        if i.isdigit():
            answer += int(i)
            lat_num = int(i)
        else:
            answer -= lat_num
        print(answer)
    return answer


a = solution("-1 -2 -3 Z")