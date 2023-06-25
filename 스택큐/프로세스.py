
def solution(priorities, location):
    answer = 0
    q = [[idx, val] for idx,val in enumerate(priorities)]
    while 1:
        save = q.pop(0)
        if any(save[1] < i[1] for i in q ):
            q.append(save)
        else:
            answer += 1 
            if save[0] == location:
                return answer
     





a = solution([1, 1, 9, 1, 1, 1], 0)
print(a)