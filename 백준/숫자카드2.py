import sys

input = sys.stdin.readline
n =int(input())
my_card =list(map(int, input().split()))
m =int(input())
card = list((map(int, input().split())))

dic = {i:0 for i in card}


for i in my_card:
    if i in dic:
        dic[i] +=1

for i in card:
    print(dic[i],end=" ")