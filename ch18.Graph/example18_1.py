
def find_parent(parent,a):
    if parent[a] != a:
        parent[a] = find_parent(parent,parent[a])
    return parent[a]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))
    
city = list(map(int,input().split()))
    
parent = [0] * (n+1)

for i in range(1,n+1):
    parent[i] = i
    
for i in range(n):
    for j in range(i,n):
        if graph[i][j] == 1:
            union_parent(parent,i+1,j+1)
            
def sol(city,parent):          
    for i in range(m-1):
        if find_parent(parent,city[i]) != find_parent(parent,city[i+1]):
            return 'NO'
        
    return 'YES'

print(sol(city,parent))


# 여행 계획에 해당하는 모든 노드가 같은 집합에 속하기만 하면 가능한 여행경로 -> 서로소 집합 알고리즘을 사용한다
