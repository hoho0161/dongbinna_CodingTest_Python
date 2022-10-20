from collections import deque


n,k = map(int,input().split())

data =[]
virus = []

for i in range(n):
    data.append(list(map(int,input().split())))
    
s,x,y = map(int,input().split())


dx=[0,0,1,-1]
dy=[1,-1,0,0]

for i in range(n):
    for j in range(n):
        if data[i][j] != 0:
            virus.append((data[i][j],0,i,j))
            
virus.sort()
q = deque(virus)

while q:
    virus, sec, i, j = q.popleft()
    if sec == s:
        break
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            if data[nx][ny] == 0:
                data[nx][ny] = virus
                q.append((virus,sec+1,nx,ny))
                

print(data[x-1][y-1])