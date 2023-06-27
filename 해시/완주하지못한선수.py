def solution(participant, completion):
    
    HashDic = {}
    sumHash = 0
    
    for i in participant:
        HashDic[hash(i)] = i
        sumHash += hash(i)
    
    for j in completion:
        sumHash -= hash(j)
    return HashDic[sumHash]



a = solution(["leo", "kiki", "eden"],	["eden", "kiki"])
print(a)