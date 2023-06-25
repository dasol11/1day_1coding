def solution(arr):
    answer = []
    for i in arr:
        if not answer:
            answer.append(i)
        elif i != answer[-1] :
            answer.append(i)

    return answer


a = [1,1,2,2,3,3,3,1,1]
print(a[-1:])
print(a[-1])
b = []
print(b[-1:])
# print(b[-1]) 
# 실행불가 IndexError: list index out of range



def solution(arr):
    answer = []
    for i in arr:
        if answer[-1:] == i: continue
        
        answer.append(i)
    return answer
