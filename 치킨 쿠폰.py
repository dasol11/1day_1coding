def solution(chicken):
    answer =0
    co =0
    while chicken !=0:
        answer += chicken // 10
        co += chicken % 10 
        print(chicken, answer, co)
        chicken = chicken // 10
        if chicken <10:
            co += chicken 
            chicken = 0
        if co >= 10:
            co -=10
            answer +=1
    return answer

a = solution(1999)
print(a)