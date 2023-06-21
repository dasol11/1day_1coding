def solution(numlist, n):
    return sorted(numlist, key = lambda x:[abs(x-n), -x])




def solution1(numlist, n):
    return sorted(numlist, key = lambda x:(abs(x-n), -x))


a = solution([10000,20,36,47,40,6,10,7000], 30)
print(a)

b = solution1([10000,20,36,47,40,6,10,7000], 30)
print(b)

c = [abs(i-30)for i in [10000,20,36,47,40,6,10,7000]]
print(c)
print(sorted(c))