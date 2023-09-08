import sys
input = sys.stdin.readline


N = int(input())

arr =[["*"]*N for _ in range(N)]

def star10(arr, s, N):
    temp = N//3
    if temp ==0:
        return
    for i in range(s[0]+temp,s[0]+temp*2):
        for j in range(s[1]+temp,s[1]+temp*2):
                arr[i][j] = " "
    
    for x in range(s[0],s[0]+N, temp):
        for y in range(s[1], s[1] + N ,temp):
            star10(arr,[x,y],temp)
            

star10(arr, [0,0], N)
for i in arr:
    print("".join(i))
            
        
        