def solution(my_string):
    stk = 0
    st = ""
    for i in my_string:
        if i.isdigit():
            st+=i
        else:
            if st :
                stk += int(st)
            st = ""      
    return stk



a = solution("aAb1B2cC34oOp")
print(a)