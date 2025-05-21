# 계단 오르기: 한 개, 두 개 까지 오를 수 있지만 3 개는 불가능
# 마지막 도착 계단은 반드시 밟아야함


# 첫번째 두번째 세번째 계단을 연속해서 모두 밟을 수 없다.

# 첫 줄에 계단의 개수
# 둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 씅있는 점수가 주어짐



n = int(input())
score = [int(input()) for _ in range(n)]
dp = [0] * n

if n <= 2:
    print(sum(score))
else:
    dp[0] = score[0]
    dp[1] = score[0] + score[1]
    for i in range(2, n):
        dp[i] = max(dp[i - 2] + score[i],
                    dp[i - 3] + score[i - 1] + score[i])
    print(dp[-1])
