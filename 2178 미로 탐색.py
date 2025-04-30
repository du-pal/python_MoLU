from collections import deque

# N과 M을 입력
N, M = map(int, input().split())
maze = []

for _ in range(N):
    row = list(map(int, input()))
    maze.append(row)

# 이동할 수 있는 4가지 방향 (위, 아래, 왼쪽, 오른쪽)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS를 위한 큐 생성
# BFS는 가까운 노드부터 차례대로 탐색해 나가는 방식
queue = deque()
queue.append((0, 0))  # 시작 지점 (0, 0) 추가

# BFS 탐색 시작
while queue:
    x, y = queue.popleft()  # 큐에서 현재 위치 꺼냄

    # 4가지 방향으로 이동 시도
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 미로 범위를 벗어나면 무시
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue

        # 벽(0)은 갈 수 없으므로 무시
        if maze[nx][ny] == 0:
            continue

        # 처음 방문하는 길(1)이면, 이전 위치의 값 + 1로 거리 저장
        if maze[nx][ny] == 1:
            maze[nx][ny] = maze[x][y] + 1
            queue.append((nx, ny))

# 도착 지점의 값을 출력 (최단 거리)
print(maze[N-1][M-1])
