T = int(input())  # 테스트 케이스 수

for _ in range(T):
    N = int(input())  # 노드 수

    parent = []
    for _ in range(N + 1):
        parent.append(0)

    depth = []
    for _ in range(N + 1):
        depth.append(-1)

    graph = []
    for _ in range(N + 1):
        graph.append([])

    # 트리 입력 받기
    for _ in range(N - 1):
        p, c = map(int, input().split())
        graph[p].append(c)
        parent[c] = p

    # 루트 노드 찾기 (부모가 없는 노드)
    root = 0
    for i in range(1, N + 1):
        if parent[i] == 0:
            root = i
            break

    # 스택으로 depth 채우기
    stack = [(root, 0)]  # (노드 번호, 깊이)
    while stack:
        node, d = stack.pop()
        depth[node] = d
        for child in graph[node]:
            if depth[child] == -1:
                parent[child] = node
                stack.append((child, d + 1))

    # 공통 조상 찾을 두 노드 입력
    a, b = map(int, input().split())

    # 깊이 맞추기
    while depth[a] > depth[b]:
        a = parent[a]
    while depth[b] > depth[a]:
        b = parent[b]

    # 동시에 부모 따라 올라가며 공통 조상 찾기
    while a != b:
        a = parent[a]
        b = parent[b]

    print(a)  
