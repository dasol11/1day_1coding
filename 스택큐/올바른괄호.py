def solution(s):
    stk = []
    try:
        for i in s:
            if i == "(":
                stk.append(i)
            else:
                stk.pop()
        if stk:
            return False
        else :
            return True
    except:
        return False


a = solution( "(()(" )
print(a)