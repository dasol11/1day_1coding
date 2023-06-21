def solution(score):
    sum_sc = [sum(i) for i in score]
    answer = [sorted(sum_sc, reverse= True).index(i)+1 for i in sum_sc ]
    
    print(sum_sc)
    print(sorted(sum_sc, reverse= True))
    return answer

a = solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]])
print(a)