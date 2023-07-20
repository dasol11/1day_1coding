import sys
input = sys.stdin.readline

def canto(arr, s ,now_l):
    temp = now_l //3
    if temp == 0:
        return
    for i in range(s+temp, s+(temp*2)):
        arr[i] = " "
        
    canto(arr, s, temp)
    canto(arr, s+temp*2, temp)
    

while True:
    try:
        n = input()
        if n == "":
            break
        else:
            n = int(n)
            arr = ["-" for _ in range(3**n)]
            canto(arr, 0, (3**n))
            print("".join(arr))
            
    except EOFError:
        break
        

