import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
start = int(input())

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

#방문여부를 저장한 리스트는 힙애서 꺼낸 정보의 거리를 가지고 함수안에서 비교후 크면 무시하는 방식으로 바뀌었다.

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))


def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
dijkstra(start)

for i in range(1,n+1):
    if distance == INF:
        print("INFINITY")
    else:
        print(distance[i])
    

#힙을 이용하여 최단거리가 가장 짧은 노드를 선택한다.