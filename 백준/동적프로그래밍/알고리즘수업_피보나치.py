import sys


def fin (n):
    if n ==1 or n ==2:
        print(1)
    else:
        return fin(n-1) + fin(n-2)