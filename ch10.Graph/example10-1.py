
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
    
for i in range(m):
    oper,a,b = map(int,input().split())
    if oper == 0:
        union_par(parent,a,b)
    elif oper == 1:
        if find_par(parent,a) == find_par(parent,b):
            print('YES')
        else:
            print('NO')
            
# 서로소 집합을 사용하여 연산
