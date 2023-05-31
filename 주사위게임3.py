def solution(a, b, c, d):
    answer = 0
    stack = [a,b,c,d]
    stack.sort()
    counts = [stack.count(i) for i in stack]
    n = max(counts)
    m = min(counts)
    if n == 4:
        answer += 1111 * a
    elif n == 3 :
        p = stack[counts.index(n)]
        q = stack[counts.index(m)]
        answer += (10*p+q)**2
    elif n == 2 and m == 2:
        p = stack[counts.index(n)]
        q = stack[counts.index(m,3)]
        answer += (p+q)* abs(p-q)
    elif n == 2 and m ==1:
        idx = counts.index(m)
        p = stack[counts.index(n)]
        q = stack[idx]za
        r = stack[counts.index(m,idx+1)]
        answer += q*r
    else:
        answer += min(stack)
    return answer