import sys
from collections import deque

# BFS 함수 정의
def BFS(a, b):
    queue = deque([a])
    visited[a] = 0  # a는 처음 시작하므로 관계 깊이는 0

    while queue:
        people = queue.popleft()  # 큐에서 한 사람을 꺼냄
        if people == b:
            return visited[b]  # b와 일치하면 그 관계 깊이 반환

        # people와 연결된 모든 사람을 확인
        for f in graph[people]:
            if visited[f] == 0:  # 아직 방문하지 않은 사람만 큐에 추가
                queue.append(f)
                visited[f] = visited[people] + 1  # 관계 깊이 +1

    return -1  # 두 사람 간에 연결이 없다면 -1 반환

input = sys.stdin.readline


n = int(input())  # 사람 수
A, B = map(int, input().split())  # 두 사람의 번호
m = int(input())  # 관계의 개수

# 그래프 초기화
graph = [[] for _ in range(n + 1)]  # 사람 번호가 1번부터 시작하므로 n+1 크기로 초기화
visited = [0] * (n + 1)  # 방문 여부와 관계 깊이를 저장할 리스트

# 부모 자식 관계 설정
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


# 결과 출력
print(BFS(A, B))
