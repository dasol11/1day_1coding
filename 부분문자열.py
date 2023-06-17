def solution(my_strings, parts):
    answer = ''
    for idx, val in enumerate(parts):
        st = my_strings[idx]
        s, e = val[0], val[1] 
        print(s,e)
        print(st)
        answer +=  st[s:e+1]
    return answer


a = solution(["progressive", "hamburger", "hammer", "ahocorasick"], [[0, 4], [1, 2], [3, 5], [7, 7]])
print(a)