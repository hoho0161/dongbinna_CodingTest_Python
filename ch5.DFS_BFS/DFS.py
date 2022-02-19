#DFS
#깊은 부분을 웃너적으로 탐색하는 알고리즘

# 크게 2가지 방식 - 인접 행렬, 인접리스트로 표현

# 인접행렬 - 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식이다. 파이썬은 2차원리스트로 구현

#인접행렬 표현방식

INF = 999999999

graph = [
    [0,7,5],
    [7,0,INF],
    [5,INF,0],
]

print(graph)

#인접리스트 - 연결리스트로 구현 파이썬은 리스트 자료형이 append()와 메소드를 제공하므로, 리스트를 사용한다.

graph_1 = [[] for _ in range(3)]

graph_1[0].append((1,7))
graph_1[0].append((2,5))

graph_1[1].append((0,7))

graph_1[2].append((0,5))

print(graph_1)

# 메모리측면  인접행렬 - 노드개수가 많을 수록 불필요한 메모리낭비,   리스트는 효율적관리
# 인접리스트는 행렬방식에 비해 두 노드가 연결되었는지 확인이 느림


#DFS 동작과정
# 1. 탐색 시작노드를 스택에 삽입 , 방문 처리
# 2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문처리를 한다. 인접노드가 없으면 스택에서 최상단 노드를 꺼낸다.
# 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i ,visited)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9

dfs(graph,1,visited)