def solution(genres, plays):
    stk = []
    dic = {key: [] for key in genres}
    for key, val in zip(genres, plays):
        dic[key].append(val)
    for i in dic.values():
        stk.append(sorted(i, reverse= True))
    
    stk.sort(key= lambda x: sum(x),reverse= True)
    answer = []
    
    for i in stk:
        for j in i[:2]:
            if i.count(j) == 2:
                for idx, v in enumerate(plays):
                    if v == j and idx not in answer :
                        answer.append(idx)
                
            else:
                answer.append(plays.index(j))

    return answer


a = solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 350, 2400, 2500])
print(a)

b = solution(["classic", "pop", "classic", "classic", "pop", "lock"], [500, 600, 150, 800, 2500, 10])
print(b)
c = solution(["classic", "pop", "classic", "classic", "pop"],[800, 600, 150, 800, 2500] )
print(c)
# c = [[10,1,1],[9,8,7]]
# c.sort(key= lambda x: sum(x),reverse= True)
# print(c)



# genres : ["classic", "pop", "classic", "classic", "pop"]
# plays : [800, 600, 150, 800, 2500]
# answer : [4, 1, 0, 3]

# 위 케이스를 고려하지 않으면 [4, 1, 3, 0]이 출력 됩니다.