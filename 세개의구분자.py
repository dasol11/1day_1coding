# 구분자가 여러개인경우 구분자를 모두 " "으로 대치해서 사용
def solution(myStr):
    answer = [x for x in myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split() if x]
    return answer if answer else ['EMPTY']