
def solution(maps):
    q = []
    q.append([0,0])
    h = len(maps)
    w = len(maps[0])
    visited = [[False]*w for _ in range(h)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited[0][0]=True
    while q:
        y, x = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < w and 0 <= ny < h and maps[ny][nx] == 1:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append([ny,nx])
                    maps[ny][nx] = maps[y][x] +1
    if maps[h-1][w-1] == 1:
        return -1
    else:
        return maps[h-1][w-1]
#[[1,0,1,1,1],
# [1,0,1,0,1],
# [1,0,1,1,1],
# [1,1,1,0,1],
# [0,0,0,0,1]]

a = solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
print(a)

b = solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1]])
print(b)