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

n = int(input())

x = []
y = []
z = []
edges = []
result = 0

for i in range(n):
    data = list(map(int,input().split()))
    x.append((data[0],i))
    y.append((data[1],i))
    z.append((data[2],i))
    
x.sort()
y.sort()
z.sort()

parent = [0]*(n+1)
for i in range(1,n+1):
    parent[i] = i
    
for i in range(n-1):
    edges.append((x[i+1][0] - x[i][0],x[i][1],x[i+1][1]))
    edges.append((y[i+1][0] - y[i][0],y[i][1],y[i+1][1]))
    edges.append((z[i+1][0] - z[i][0],z[i][1],z[i+1][1]))
    
edges.sort()


for edge in edges:
    cost, x, y = edge
    if find_par(parent,x) != find_par(parent,y):
        union_par(parent,x,y)
        result += cost
        
        
print(result)