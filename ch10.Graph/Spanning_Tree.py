# 신장트리 - 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프를 의미

# 최소한의 비용으로 신장트리를 찾아야 할 때가 필요 - 최소 신장 트리 알고리즘으로 크루스칼 알고리즘이 존재한다.
# 크루스칼 알고리즘은 그리디 알고리즘으로 분류됨 - 모든 간선에 대하여 정렬을 수행한 뒤 가장 거리가 짧은 간선부터 집합에 포함시킨다.

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    

v, e = map(int,input().split())
parent = [0] * (v+1)

for i in range(1,v+1):
    parent[i] = i

edges = []
result = 0

for _ in range(e):
    a, b, cost = map(int,input().split())
    edges.append((cost,a,b))
    
edges.sort()

for edge in edges:
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
        
print(result)

# 크루스칼 알고리즘의 시간 복잡도 - 간선 개수가 E개 일때 O(ElogE)의 시간복잡도를 가짐 - 간선 정보를 정렬하는데에 걸리는 시간이 대부분이다.