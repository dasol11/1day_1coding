import sys
input = sys.stdin.readline


def cantor (arr, s,now):
    temp = now//3
    
    if temp  == 0:
        return
    for i in range(s+temp,s+(temp*2)):
        arr[i] = " "
        
    cantor(arr, s,temp )
    cantor(arr, s+temp*2, temp)
       
    
while True:
    
    try:
        N= int(input())
        arr = ["-"]*(3**N)
        cantor(arr, 0 , 3**N)    
        print("".join(arr))
    except:
        break
    
