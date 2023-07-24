import sys
input = sys.stdin.readline

N = int(input())
row = [0] * N
answer = 0
def is_promising(x):
    for i in range(x):
        if row[i] == row[x] or abs(row[x]-row[i]) == abs(x-i):
            return False
    else:
        
        return True
    
    
def n_qeens(x):
    global answer
    if x == N:
        answer += 1
        return
    else:
        for i in range(N):
            row[x] = i
            if is_promising(x):
                n_qeens(x+1) 
                

n_qeens(0)
print(answer)