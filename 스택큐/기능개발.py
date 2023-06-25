# 내 코드
def solution(progresses, speeds):
    answer = []
    check = [False for _ in range(len(progresses))]
    m = 0
    n = 1
    while not all(check):
    
        for idx, val in enumerate(progresses):
            if not check[idx]:
                val += speeds[idx]
                progresses[idx] = val
                if val >= 100 :
                    check[idx] = True
       
        if check[m] :
            for i in check[m+1:]:
                
                if i :
                    n += 1
                else:
                    m += n
                    answer.append(n)
                    n = 1
                    break
    answer.append(n)
    return answer

a = solution([93, 30, 55], [1, 30, 5])

b = solution( [95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])

def solution1(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        print(p,s, Q)
        print(((100-p)//s))
        if len(Q)==0 or Q[-1][0]< ((100-p)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]


c = solution1( [95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
d = solution1([93, 30, 55], [1, 30, 5])
print(d)
print(- (30-100)//30)