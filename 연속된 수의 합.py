def solution(num, total):
    
    for i in range(-(total+num), (total+num) ):
        sum = 0
        answer = []
        for j in range(num):
            sum += (i+j)
            answer.append(i+j)
        if sum == total:
            break
            
    return answer



a = solution(3,0)
print(a)