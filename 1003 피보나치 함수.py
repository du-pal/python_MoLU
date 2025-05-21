# 다이나믹 프로그래밍 
# 필요한 계산 값을 저장해두었다가 재사용하는 알고리즘 설계 기법이다.

# 큰 문제를 한번에 해결하기 어려울 때, 여러개의 작은 문제로 나누어 푸는 '분할 정복' 
# 알고리즘이 있다. 
# 이때 동일한 작은 문제들이 반복적으로 계산되는 경우가 생길 수 있다. 
# 그 문제를 매번 재계산 하지 않고 값을 저장했다가 재사용하는 기법이 바로 다이나믹 프로그래밍이다. 
# 메모리 공간을 약간 더 사용하여 시간을 획기적으로 줄일 수 있는 방법이다.


def fib(N):
    zeros = [1, 0, 1]  # zeros[i]: fib(i)를 호출했을 때 0이 출력된 횟수
    ones =  [0, 1, 1]  # ones[i]:  fib(i)를 호출했을 때 1이 출력된 횟수

    if N >= 3:
        for i in range(2,N):
            zeros.append(zeros[i-1] + zeros[i])
            ones.append(ones[i-1] + ones[i])
    print(f"{zeros[N]} {ones[N]}")
 
T = int(input())
for _ in range(T):
    N = int(input())
    fib(N)
