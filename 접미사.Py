def solution(my_string):
    answer = []
    rev_str = my_string[::-1]
    print(rev_str)
    for i in range(len(rev_str)):
        answer.append(rev_str[:i+1])
    return answer

a= solution("banana")
print(a)