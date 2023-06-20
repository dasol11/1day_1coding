def solution(my_str, n):
    
    return [my_str[i:i+n] for i in range(0, len(my_str),n)]



a = solution("abc1Addfggg4556b",	6)

print(a)

# for문을 이용해서 인덱스를 지정하는게 예술
