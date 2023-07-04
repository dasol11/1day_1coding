n,m=map(int,input().split())

st = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer = []
while n != 0:
    answer.append(st[n % m])
    n = n//m
answer.reverse()
print("".join(answer))
