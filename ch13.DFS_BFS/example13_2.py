n,m = map(int,input().split())

data = []
temp = [[0]*m for _ in range(n)]

for i in range(n):
    data.append(list(map(int,input().split())))

res = 0

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def score():
    v = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                v+=1
    return v

def virus(i,j):
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if nx >= 0 and nx<n and ny>=0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx,ny)
            
    

def dfs(cnt):
    global res
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
                
        for i in range(n):
            for j in range(m):      
                if temp[i][j] == 2:  
                    virus(i,j)
        res = max(res,score())
        return
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                cnt+=1
                dfs(cnt)
                data[i][j] = 0
                cnt-=1
                
dfs(0)
print(res)