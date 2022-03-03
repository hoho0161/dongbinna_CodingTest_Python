import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n,m,c = map(int,input().split())

graph = [[] for i in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
    x,y,cost = map(int,input().split())
    graph[x].append((y,cost))
    
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    
    
    while q:
        #dist는 출발지점-> 큐에서꺼낸 노드까지의 거리
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            # now를 거쳐 i[0]에 도착하는 거리
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                
                
dijkstra(c)

count = 0
max_dist = 0

for city_dist in distance:
    if city_dist != INF:
        count += 1
        max_dist = max(max_dist, city_dist)
        
#시작도시는 제외
print(count-1,max_dist)
