def solution(myString):
    answer = []
    st = ""
    for i in myString:
        if i != "x":
            st += i
        else:
            if st :
                answer.append(st)
            st = ""
    answer.sort()
    return answer

a = solution("xaxbxcxdx")
print(a)


# 모범답안
def solution(myString):
    return sorted(ch for ch in myString.split('x') if ch)
## ""을 없애주기 위해서 조건문 if ch를 추가해준다.