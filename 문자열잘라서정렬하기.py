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