#BFS 문제

from collections import deque

n, m =  map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        #큐에서 꺼내오기
        x, y = queue.popleft()
        
        #4방향으로 확인하기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            #인덱스 범위 체크하기
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            #그래프에서 벽일때
            if graph[nx][ny] == 0:
                continue
            
            #처음으로 방문했을 때
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
        
    return graph[n-1][m-1]

print(bfs(0,0))