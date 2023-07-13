import sys

input = sys.stdin.readline

t = int(input())

stk = [int(input()) for _ in range(t)]
print(stk)
stk.sort()

print(round(sum(stk)/t))
print(stk[t//2])

dic = {}
for i in stk:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
max_val = max(dic.values())
max_list = []
for j in dic.keys():
    if dic[j] == max_val :
        max_list.append(j)

if len(max_list) >1:
    print(max_list[1])
else:
    print(max_list[0])

print(max(stk)- min(stk))
    