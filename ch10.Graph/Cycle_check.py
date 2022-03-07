#무방향 그래프의 경우 서로소 집합을 활용한 판별
# 1각 간선을 확인하며 두 노드의 루트 노드를 확인한다.
#   -다르면 두 노드 union , 같다면 사이클 발생
# 2모든 간선에 대하여 반복

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

cycle = False

for i in range(e):
    a, b =map(int,input().split())
    if find_parent(parent,a) == find_parent(parent,b):
        cycle = True
        break
    else:
        union_parent(parent,a,b)
        
        
if cycle:
    print("사이클 발생")
else:
    print("사이클 발생x")

