def find_par(parent,x):
    if parent[x] != x:
        parent[x] = find_par(parent,parent[x])
    return parent[x]

def union_par(parent,x,y):
    x = find_par(parent,x)
    y = find_par(parent,y)
    
    if x < y:
        parent[y] = x
    else:
        parent[x] = y



n, m = map(int,input().split())

result=0
max_cost = 0
edges = []

parent = [0]*(n)
for i in range(0,n):
    parent[i] = i
    
for _ in range(m):
    x, y, cost = map(int,input().split())
    max_cost += cost
    edges.append((cost,x,y)) # 정렬을 위해 cost를 앞으로 빼줌

edges.sort() # 오름차순이므로 cost가 작은것 부터 정렬됨

for edge in edges:
    cost, x, y = edge
    if find_par(parent,x) != find_par(parent,y):
        union_par(parent,x,y)
        result += cost 


print(max_cost - result) #절약한 금액을 구해야 하므로 전체비용에서 구한최소비용을 빼준다