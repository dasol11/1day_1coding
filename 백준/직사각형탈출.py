x, y, w, h = map(int,input().split())

stk = [x,y, (w-x), (h-y)]
print(min(stk))