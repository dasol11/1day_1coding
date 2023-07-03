stk = []
m = 0
idx = ["1","1"]
for i in range(1,10):
    li = list(map(int,input().split()))
    m_li = max(li)
    if m_li > m:
        m = m_li
        idx = [str(i), str(li.index(m)+1)]
        
print(m)
print(" ".join(idx))