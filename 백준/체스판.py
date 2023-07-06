y,x = map(int, input().split())
board = []
answer = []

for _ in range(y):
    board.append(input())
    
for i in range(y-7):
    for j in range(x-7): # (i,j) 시작점 지정
        ans1 , ans2 = 0 , 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if board[a][b] == "W":
                        ans1 +=1
                    if board[a][b] == "B":
                        ans2 +=1
                else:
                    if board[a][b] == "B":
                        ans1 +=1
                    if board[a][b] == "W":
                        ans2 +=1
        answer.append(ans1)
        answer.append(ans2)

print(min(answer))
        