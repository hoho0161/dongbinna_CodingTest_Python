import heapq

INF = 987654321

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    v1, v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    
distance[1] = 0
q = [(0,1)]

while q:
    dist, now = heapq.heappop(q)
    
    if distance[now] < dist :
        continue
    
    for i in graph[now]:
        cost = dist + 1
        
        if cost < distance[i] :
            distance[i] = cost
            heapq.heappush(q,(cost,i))
            

max_idx = 1
max_dist = 0
max_count = 0

for i in range(2,n+1):
    if distance[i] > max_dist:
        max_idx = i
        max_count = 1
        max_dist = distance[i]
    elif distance[i] == max_dist:
        max_count += 1
        
print(max_idx,max_dist,max_count)


# heapq.heappush 부분에서 i가 아닌 now로 적어두고 계속 찾고 있었다. 좀 더 꼼꼼히 확인하거나 변수를 확실히 지정해줘야겠다.

