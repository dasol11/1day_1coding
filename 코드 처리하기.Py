def solution(code):
    answer = ''
    mode = 0
    for idx, val in enumerate(code):
        if val== "1" and mode == 0:
            mode += 1
        elif val =="1" and mode == 1:
            mode -= 1
            
        else:
            if mode == 0:
                if idx %2 ==0:
                    answer += val
            elif mode == 1:
                if idx %2 !=0:
                    answer += val
    return answer


a = solution("abc1abc1abc")
print(a)