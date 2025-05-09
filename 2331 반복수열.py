A, P = map(int, input().split())  # A는 시작 수, P는 자릿수를 몇 번 곱할 것인지를 받음

result = [A]  # 수열을 저장할 리스트, 처음 값 A를 추가

while True:
    num = 0
    # 마지막 수(result[-1])의 각 자릿수에 대해 P번 곱한 값을 합산
    for i in str(result[-1]):
        num += int(i) ** P
        
    if num in result:  # 수열에 이미 num이 있다면 반복이 시작되었으므로 종료
        break
    
    result.append(num)  # 반복되지 않으면 num을 수열에 추가

# result[0]는 A 값이므로 [1]부터 반복이 시작되는 마지막 인덱스까지의 번호가 
# 수열에 남게 되는 수들의 개수와 같다.
print(result.index(num))
