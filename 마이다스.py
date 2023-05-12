

def solution(S):
    
    dic = {')' : '(', ']' : '[', '}': '{'}

    stack = []
    num = S.count('/*')
    
    for i in range(num):
        st = S.find('/*')
        end = S.find('*/')+ 2
        S = S[:st] + S[end:]
        
    for char in S:

        if (char in '({['):
    
            stack.append(char)


        else:

            if (stack):

                top = stack.pop()

                if (dic[char] != top):
                    answer = "TRUE"

            else:
                answer = "FALSE"
    answer = "TRUE"
    return answer

print(solution("{{}}"))
print(solution("({})[]"))
print(solution("[)"))
print(solution("]()["))
print(solution("([())]"))
