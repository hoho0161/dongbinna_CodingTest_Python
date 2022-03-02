import sys
input = sys.stdin.readline
INF = int(1e9) # 10억

n,m = map(int,input().split())
start = int(input())

# 초기 설정할 리스트들
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int,input().split()) # a번 노드에서 b번 노드로 가는 비용이 c임
    graph[a].append((b,c))


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
            
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    #시작노드 간선에 대한 갱신
    for j in graph[start]:
        distance[j[0]] = j[1]
    
    #시작노드제외 모든노드를 방문하기
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                
dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
        
        

#쉬운버젼의 다익스트라 알고리즘 O(V^2)의 시간복잡도를 가진다.