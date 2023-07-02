n, m = map(int,(input().split()))
basket = ["0" for _ in range(n)]
for _ in range(m):
    s, e, val = map(int,(input().split()))
    for i in range(s,e+1):
        basket[i-1] = str(val)
s = " ".join(basket)
print(s)
