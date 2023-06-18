def solution(date1, date2):
    answer = 0
    if date1[0] < date2[0]:
        answer = 1
    else:
        if date1[1] < date2[1]:
            answer =1 
        else:
            if date1[2] < date2[2]:
                answer =1
            else:
                answer = 0
    return answer

a = solution([2021, 12, 31], [2022, 1, 1])
print(a)
#date1[i] < date2[i]가 아닌 경우에 그냥 넘어가고 있는데요 이렇게 하면 2010.2.10 과 2009.12.10일 때 동작을 보면


# 미친 답안 
def solution(date1, date2):
    return int(date1 < date2)
