import heapq
import sys
input = sys.stdin.readline  # 입력을 빠르게 처리

N = int(input())  # 입력 받을 연산 횟수 N

input_list = []  # 힙을 저장할 리스트

for _ in range(N):
    x = int(input())
    
    if x != 0:
        heapq.heappush(input_list, -x)  # 음수로 변환하여 삽입 (최대 힙처럼 동작하게)
    else:
        if input_list:  # 리스트에 값이 있으면
            max_value = -heapq.heappop(input_list)  # 가장 큰 값 꺼내기 (음수를 다시 양수로 변환)
            print(max_value)
        else:
            print(0)
