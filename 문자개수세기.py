def solution(my_string):
    answer = [0 for _ in range(26)]
    for i in my_string:
        if i.isupper():
            answer[ord(i)-65] += 1
        else:
            answer[ord(i)-97] +=1
    return answer


a = solution("Programmers")
print(a)