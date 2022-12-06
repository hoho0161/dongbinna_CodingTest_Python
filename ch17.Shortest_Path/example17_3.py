import heapq
INF = 1e9

dx = [-1,0,1,0]
dy = [0,1,0,-1]


def search(n,data):
    x = 0
    y = 0
    distance = [[INF]*(n) for _ in range(n)]
    q = [(data[x][y],x,y)]
    distance[x][y] = data[x][y]
    
    while q:
        dist, x, y =heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + data[nx][ny]
            
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q,(cost,nx,ny))
                
    return distance[n-1][n-1]
    
                

test_case = int(input())

for _ in range(test_case):
    n = int(input())
    data = []
    for _ in range(n):
        data.append(list(map(int,input().split())))
        
    res = search(n,data)
    print(res)
    
    
# 다익스트라 문제로 heapq를 사용해 시간복잡도 개선효과를 위해 작성법을 손에 더 익혀야 겠다