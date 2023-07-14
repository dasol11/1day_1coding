import sys

input = sys.stdin.readline


while True:
    
    st = input()
    stk = []
  
    if st[0]== ".":
        break
    for i in st:
        if i == "(" or i == "[":
            stk.append(i)
        elif i == ")" :
            if stk and stk[-1] =="(":
                stk.pop()
            else:
                print("no")
                break
        elif i == "]" :
            if stk and stk[-1] =="[":
                stk.pop()
            else:
                print("no")
                break
    else:
        if stk : 
            print("no")
        else:
            print("yes")