
def sol( N, li):
    x = 1
    y = 1
    S = li.split()
    for i in range(N+1):
        if S[i] == "R" and y !=100 :
            y +=1
        
        elif S[i] == "L" and y != 1 :
            y -= 1
        
        elif S[i] == "U" and x != 1:
            x -= 1
        
        elif S[i] == "D" and x != 100:
            x += 1
        print(x, y)
    return (x, y)

def sol2 ( N, li):
    x = 1
    y = 1
    S = li.split()
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move = ["L", "R", "U", "D"]
    for s in S:
        for i in range(len(move)):
            if s == move[i]:
                nx = x + dx[i]
                ny = y + dy[i] 
        
        if 1 <= nx <=100 and 1<= ny<=100:
            x = nx
            y = ny
    return(x,y)
    
#a = sol(5, "R R R U D D")
#print(a)

b = sol2(5, "R R R U D D")
print(b)