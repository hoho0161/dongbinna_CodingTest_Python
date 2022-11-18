from collections import deque

n,l,r = map(int,input().split())

m=[]
for i in range(n):
    m.append(list(map(int,input().split())))
    
result = 0

dx = [-1,0,1,0]
dy = [0,-1,0,1]


def process(x,y, index):
    united = [] #연합인 왕국 위치를 저장하여 후에 인구수 조정
    united.append((x,y))
    q = deque()
    q.append((x,y))
    union[x][y] = index
    summary = m[x][y]
    count = 1
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1: # union[nx][ny]== -1 은 값을 변경했을때 다른 왕국에서 검사시 같은 연합으로 인식되는 것을 방지 
                if l <= abs(m[nx][ny] - m[x][y]) <= r: # 절대값
                    q.append((nx,ny))
                    union[nx][ny] = index
                    summary += m[nx][ny]
                    count += 1
                    united.append((nx,ny))
            
    for i,j in united:
        m[i][j] = summary // count
    return count
        

total_count = 0

while True:
    union = [[-1]*n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i,j,index)
                index += 1
    
    if index == n*n:
        break
    total_count += 1
    
print(total_count)

