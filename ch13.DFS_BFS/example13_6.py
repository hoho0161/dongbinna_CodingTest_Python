n = int(input())

m = []

for i in range(n):
    m.append(list(input().split()))

def isAvoid(m):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for i in range(n):
        for j in range(n):
            if m[i][j] == 'T':
                for k in range(4):
                    posx = i + dx[k]
                    posy = j + dy[k]
                    while posx  >= 0 and posx < n and posy  >=0 and posy  < n:
                        if m[posx][posy] == 'O':
                            break
                        if m[posx][posy] == 'S':
                            return False
                        
                        posx += dx[k]
                        posy += dy[k]
    
    return True
    
def dfs(ob,m):
    if ob == 3:
        if isAvoid(m):
            return True
        else:
            return False
    else:
        for i in range(n):
            for j in range(n):
                if m[i][j] == 'X':
                    m[i][j] = 'O'
                    if dfs(ob+1,m):
                        return True
                    m[i][j] = 'X'
    
        return False

if dfs(0,m):
    print('YES')
else:
    print('NO')
    
# DFS/BFS의 전형적인 문제라고 생각한다,만약 입력조건이 이 문제보다 클 경우 실행시간을 줄일 수 있는 부분을 생각해보자
# itertools의 combinations 로 'X'의 위치만 조합하여 확인할 수도 있다