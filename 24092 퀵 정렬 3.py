import sys
sys.setrecursionlimit(10000)

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)

def partition(A, p, r):
    global found
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
            if A == B:
                found = True
    if i + 1 != r:
        A[i + 1], A[r] = A[r], A[i + 1]
        if A == B:
            found = True
    return i + 1

# 입력 처리
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

found = False
quick_sort(A, 0, N - 1)

if found:
    print(1)
else:
    print(0)

