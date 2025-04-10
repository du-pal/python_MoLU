# 블랙잭 양의 정수로 쓰여짐
# 딜러는 n장의 카드를 모두 숫자가 보이게 바닥으로 놓고 딜러가 숫자 M 을 외친다.
# 플레이어는 제한 된 시간 안네 N장 중 3장을 뽑는다.
# 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 가깝게 만들어야함
# N장의 카드에 써져 있는 숫자가 주어졌을 때 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력

# N M을 입력 받는다
# 카드 N 장을 입력 받는다.
# N장 중 3장의 합이 M과 유사하게 만들어야함

N, M = map(int,input().split())
nums = list(map(int, input().split()))

max_sum_like_M = 0 # 가장 큰 값 저장
sum_like_M = 0 # 현재의 3장의 카드의 합

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum_like_M = nums[i]+nums[j]+nums[k]
            if sum_like_M <= M:
                max_sum_like_M = max(max_sum_like_M,sum_like_M)
                # 3장의 합 중 가장 큰 것을 구하는 것을 max_로 놓고 계속 반복
                # 만약 max_보다 큰 값이 있으면 그것을 새롭게 max_로 지정
            else:
                continue

print(max_sum_like_M)
