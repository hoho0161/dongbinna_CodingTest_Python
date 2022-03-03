# 모든지점에서 다른 모든 지점까지 최단경로를 모두 구해야 하는 경우 사용
# 다이나믹 프로그래밍 특징 - 노드개수 N 일 때 N번만큼 반복하며 점화식에 맞게 2차원 리스트를 갱신하기 때문이다.
# O(N^3) 시간복잡도를 가진다.

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기자신비용 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

#간선정보로 초기화
for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a][b] = c

# 점화식
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k] + graph[k][b])
            
            
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:
            print("INF", end=' ')
        else:
            print(graph[a][b],end=' ')
    print()
    
