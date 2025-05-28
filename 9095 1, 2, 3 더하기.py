n = int(input())

arr = [0] * 11  # arr[i] = i를 1,2,3의 합으로 만드는 방법 수
arr[1] = 1      # 1 => [1]
arr[2] = 2      # 2 => [1+1], [2]
arr[3] = 4      # 3 => [1+1+1], [1+2], [2+1], [3]

# 점화식: arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
for i in range(4, 11):
    arr[i] = arr[i-1] + arr[i-2] + arr[i-3]

# 테스트케이스 개수만큼 입력받고 출력
for i in range(0, n):
    test = int(input())
    print(arr[test])
