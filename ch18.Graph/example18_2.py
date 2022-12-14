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



g = int(input())
p = int(input())

parent = [0] * (g+1)

for i in range(1,g+1):
    parent[i] = i

res = 0

data = []
for i in range(p):
    data.append(int(input()))

for i in range(p):
    if find_parent(parent,data[i]) == 0:
        break
    
    
    for j in range(data[i],0,-1):
        if find_parent(parent,j) == j:
            union_parent(parent,j,j-1)
            res+=1
            break
    
    
    
print(res)
    
        
