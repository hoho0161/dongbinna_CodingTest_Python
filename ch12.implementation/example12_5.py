n = int(input())
k = int(input())
info = []
drow = [0,1,0,-1]
dcol = [1,0,-1,0]

m = [[0]*(n+1) for _ in range(n+1)]

for i in range(k):
    row, col = map(int,input().split())
    m[row][col] = 1
    
l = int(input())
for i in range(l):
    time, comm = input().split()
    info.append((int(time),comm))
    

def turn(direction,c):
    if c == "L":
        direction = (direction -1)%4
    else:
        direction = (direction +1)%4
        
    return direction

def solution():
    x,y = 1,1
    m[x][y] = 2
    direction = 0
    idx = 0
    time = 0
    q = [(x,y)]
    
    while True:
        nx = x + drow[direction]
        ny = y + dcol[direction]
        
        if 1 <= nx and nx <= n and 1<= ny and ny <= n and m[nx][ny] != 2:
            # 사과x
            if m[nx][ny] == 0:
                m[nx][ny] = 2
                q.append((nx,ny))
                px, py = q.pop(0)
                m[px][py] = 0
            if m[nx][ny] == 1:
                m[nx][ny] = 2
                q.append((nx,ny))
                
        else:
            time += 1
            break
        
        x,y = nx,ny
        time += 1
        if idx < l and time == info[idx][0]:
            direction = turn(direction,info[idx][1])
            idx += 1
        
    
    return time
            
            
       
print(solution())
    

#오른쪽 - 시계
#왼쪽 - 반시계    