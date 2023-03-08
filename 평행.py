
"""
https://school.programmers.co.kr/learn/courses/30/lessons/120875#qna

초반에 테스트 5번이 통과되지 못해서 고생했다 
and를 or 로 바꿔서 통과했다 

"""

def solution(dot):
    answer = 0
    a = (dot[1][1]-dot[0][1])/(dot[1][0]-dot[0][0])
    b = (dot[3][1]-dot[2][1])/(dot[3][0]-dot[2][0])
    
    
    c = (dot[2][1]-dot[0][1])/(dot[2][0]-dot[0][0])
    d = (dot[3][1]-dot[1][1])/(dot[3][0]-dot[1][0])
    
    if a == b or c == d : # or 부분을 처음에 and로 해서 고생함
        answer = 1
        
    return answer