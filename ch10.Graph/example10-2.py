
def find_par(parent,x):
    if parent[x] != x:
        parent[x] = find_par(parent,parent[x])
    return parent[x]

def union_par(parent,a,b):
    a = find_par(parent,a)
    b = find_par(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
        
    
n,m = map(int,input().split())
parent = [0] * (n+1)

for i in range(0,n+1):
    parent[i] = i
    
edges = []
result = 0

for _ in range(m):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))
    
edges.sort()
last = 0

for edge in edges:
    cost ,a ,b = edge
    if find_par(parent,a) != find_par(parent,b):
        union_par(parent,a,b)
        result += cost
        last = cost

print(result - last)

# 최소신장트리를 크루스칼 알고리즘으로 구한뒤 가장 큰 간선만 뽑아내면 마을 2개를 만들수 있다. 사이클은 서로소집합을 이용하여 판별한다.
