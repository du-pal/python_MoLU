# 소수: 자기 자신과 1로 나눴을때만 나머지가 0이 나옴
N = int(input())


count = 0
nums = list(map(int, input().split()))



for i in range(N):  
    num = nums[i] #그냥 list 안에서 돌려도 될거 같은데,,, N을 사용해야하니...

    if num < 2:
        continue
    
    for j in range(2,num):
        if num % j == 0:  # 소수가 아니다. -> for 반복문 멈추고 +1 됨.
            break
        
    else:
        count += 1

print(count)
