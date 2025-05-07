from collections import deque

# 입력 받기
F, S, G, U, D = map(int, input().split())

# 방문 여부와 이동 횟수 기록용 리스트
visited = [False] * (F + 1)
dist = [0] * (F + 1) # 각 층까지 누른 버튼 수를 저장 (최단 거리)

# BFS 시작
queue = deque()
queue.append(S)
visited[S] = True # 방문함

while queue:
    current = queue.popleft()

    if current == G:  # 목표 층에 도달했으면
        print(dist[current])
        break

    # 이동할 수 있는 두 방향: 위로 U, 아래로 D
    for next_floor in (current + U, current - D):
        # 유효한 층이고 아직 방문하지 않았다면
        if 1 <= next_floor <= F and not visited[next_floor]:
            visited[next_floor] = True
            dist[next_floor] = dist[current] + 1
            queue.append(next_floor)
else:
    # while문이 끝났지만 G에 도달하지 못한 경우
    print("use the stairs")
