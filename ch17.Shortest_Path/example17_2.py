n,m = map(int,input().split())

INF = 1e9

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j :
            graph[i][j] = 0

for _ in range(m):
    a, b = map(int,input().split())
    graph[a][b] = 1
    
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
            
res = 0

for i in range(1,n+1):
    count = 0
    for j in range(1,n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count+=1
        
    if count == n:
        res += 1
        
print(res)
    
    
# 비교순위를 알기 위해서는 두명간 연결된 경로가 있어야 한다
# 모든 사람에 대해 정확한순위여부를 알아야 하므로 플로이드워셜 알고리즘으로 구현한다 N<=500 이므로 O(n^3) 알고리즘을 사용할 수 있다