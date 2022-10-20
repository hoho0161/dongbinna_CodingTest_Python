from collections import deque
import sys
input=sys.stdin.readline

n,m,k,x = map(int,input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])

while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)
            
check = False
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        check = True
        
if check == False:
    print(-1)


# 모든 간선의 비용이 동일한 경우 BFS를 통해 최단 거리를 찾을 수 있다
# 거리가 1인 노드를 찾은후 2인 노드 -> 3인 노드 -> .. 이기때문에 가능하다