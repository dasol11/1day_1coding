def solution(before, after):
    print(sorted(before))
    print(sorted(after))
    
    return 1 if sorted(before) == sorted(after) else 0


a = solution("abc", "dca")