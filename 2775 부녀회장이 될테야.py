t = int(input())

for i in range(t):
    k = int(input())        # 층
    n = int(input())        # 호
    people = [i for i in range(1, n+1)]     # 0층: 1명, 2명, ..., n명

    for x in range(k):
        new = []
        for y in range(n):
            new.append(sum(people[:y+1]))   # 아래층의 1~n호까지 누적합
        people = new.copy()  # 현재 층 정보 업데이트
    print(people[-1])        # k층 n호의 사람 수
