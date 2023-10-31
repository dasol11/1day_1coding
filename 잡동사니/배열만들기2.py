"""

True and Ture 일때만 조건문을 수행함
즉, if j !="5" and j !="0":
이 문장은 0과 5의 모두 아닐때, 즉 j !="5"와 j !="0"가 모두 Ture일때 실행되는 조건문이다.


"""


def solution(l, r):
    answer = []
    for i in range(l,r+1):
        if i % 5 ==0:
            is_five_or_zero = True
            for j in str(i):
                if j !="5" and j !="0":
                    is_five_or_zero = False
                
            if is_five_or_zero:
                answer.append(i)
    if not answer:
        answer.append(-1)

    return answer

a = solution(40,60)
print(a)
