def solution(A, B):
    stk = [A[i:]+A[:i] for i in range(len(A),0,-1)]
    return stk.index(B) if B in stk else -1


a= solution("hello","ohell")
print(a)



solution=lambda a,b:(b*2).find(a)
# find()는 문자열에서 해당 문자를 찾아주고 없으면 -1을 반환한다는 특징을 이용함

#"ohellohell" 에서 "hello"를 찾으면 이동한 거리를 찾아주고 없으면 -1 반환 ㄱ
# 진짜 미친코드이다.
