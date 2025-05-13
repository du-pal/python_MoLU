n, k = map(int, input().split())  # n, k 값을 입력받음
nums = list(map(int, input().split()))  # nums 배열을 입력받음

count = 0  # 교환 횟수
answer = -1  # 교환이 k번 이루어지지 않으면 -1을 출력

for i in range(n - 1):  # 앞에서부터 버블 정렬을 수행
    for j in range(n - 1 - i):  # 두 요소를 비교해서 교환
        if nums[j] > nums[j + 1]:
            count += 1
            nums[j], nums[j + 1] = nums[j + 1], nums[j]  # 교환

            # k번째 교환이 발생한 후 배열을 기록
            if count == k:
                answer = nums[:]  # 교환 직후 배열의 복사본을 저장
                break  # k번째 교환 후 더 이상 진행할 필요 없음

    if answer != -1:  # 이미 k번째 교환을 찾았다면 외부 루프 종료
        break

# k번째 교환이 발생한 경우 배열을 출력, 그렇지 않으면 -1 출력
if isinstance(answer, list):  # answer가 리스트이면
    print(*answer)  # 리스트의 요소들을 공백으로 구분하여 출력
else:
    print(answer)  # 교환이 부족하면 -1을 출력
