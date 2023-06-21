def solution(n):
    answer = 0
    m = 0
    while n > m:
        print(m, answer,"start")
        m += 1
        answer += 1
        if answer % 3 ==0:
            answer += 1
        else:
            for i in str(m):
                if i == "3":
                    answer +=1  
        
        if answer % 3 ==0:
            answer +=1
        print(m, answer)    
    return answer

a = solution(15)