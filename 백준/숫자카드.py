import sys

input = sys.stdin.readline
n =int(input())
my_card = list(map(int, input().split()))
m =int(input())
card = list(map(int, input().split()))

dic = {i:0 for i in my_card }

for i in range(m):
    if card[i] in dic:
        print("1",end=" ")
    else:
        print("0",end=" ")