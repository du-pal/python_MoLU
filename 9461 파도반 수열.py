import sys
input = sys.stdin.readline

MAX = 101 
arr = [0, 1, 1, 1] + [0 for _ in range(MAX - 4)]

def func(x):
    if arr[x]:
        return arr[x]
    else:
        arr[x] = func(x-2) + func(x-3)
        return arr[x]

t = int(input())
for _ in range(t):
    n = int(input())
    print(func(n))
