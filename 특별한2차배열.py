def solution(n):
    return [[1 if i == j else 0 for j in range(n) ] for i in range(n)]


a = solution(6)

print(a)


#True or False 는  int 메서드를 활용하면 1 or 0 으로 변환된다 