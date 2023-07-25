import sys
input = sys.stdin.readline

graph = [list(map(int,input().split())) for _ in range(9)]

blank = [(i,j)for i in range(9) for j in range(9) if graph[i][j] == 0]

def check_low (x, a):
    for i in range(9):
        if graph[x][i] == a:
            return False
    else:
        return True
    
def check_col(y, a):
    for i in range(9):
        if graph[i][y] == a:
            return False
    else:
        return True

def check_rec(x,y,a):
    nx = x//3*3
    ny = y//3*3
    
    for i in range(3):
        for j in range(3):
            if graph[nx+i][ny+j] == a:
                return False
    else:
        return True
                
def dfs(idx):
    
    if idx == len(blank):
        for i in graph:
            print(" ".join(map(str,i)))
        exit(0)
    
    for j in range(1,10):
        x = blank[idx][0]
        y = blank[idx][1]
        if check_low(x,j) and check_col(y,j) and check_rec(x,y,j):
            graph[x][y] = j
            dfs(idx+1)
            graph[x][y] = 0

dfs(0)