"""

math를 쓰면 쉽게 해결하지만
수식을 정리해서 해곃
"""



def solution(balls, share):
    n = 1
    m = 1
    for i in range(balls, share,-1):
        n *= i
    for j in range(1,balls-share+1):
        m *= j
    return n/m