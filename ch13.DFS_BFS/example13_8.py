from collections import deque

def solution(board):
    visit = [[[False]*2 for _ in range(101)] for _ in range(101)]
    N = len(board)
    q = deque()
    q.append([[0,1],[0,0]])
    visit[0][1][0] = True
    
    while q:
        qq = q.popleft()
        x = qq[0][0]
        y = qq[0][1]
        shape = qq[1][0]
        cnt = qq[1][1]
        
        if x==N-1 and y==N-1:
            return cnt
        
        if shape == 0: # 가로모양
            #오른쪽
            if y+1<N and board[x][y+1] == 0:
                if not visit[x][y+1][shape]:
                    visit[x][y+1][shape] = True
                    q.append([[x,y+1],[shape,cnt+1]])
            #왼쪽
            if y-2>=0 and board[x][y-2] == 0:
                if not visit[x][y-1][shape]:
                    visit[x][y-1][shape] = True
                    q.append([[x,y-1],[shape,cnt+1]])
            #아래
            if x+1<N and y-1>=0 and board[x+1][y] == 0 and board[x+1][y-1] ==0:
                if not visit[x+1][y][shape]:
                    visit[x+1][y][shape] = True
                    q.append([[x+1,y],[shape,cnt+1]])
            #위
            if x-1>=0 and y-1>=0 and board[x-1][y] == 0 and board[x-1][y-1] ==0:
                if not visit[x-1][y][shape]:
                    visit[x-1][y][shape] = True
                    q.append([[x-1,y],[shape,cnt+1]])
            #회전
            if x+1<N and y-1>=0 and board[x+1][y] == 0 and board[x+1][y-1] ==0:
                if not visit[x+1][y-1][int((shape+1)%2)]:
                    visit[x+1][y-1][int((shape+1)%2)] = True
                    q.append([[x+1,y-1],[int((shape+1)%2),cnt+1]])
                if not visit[x+1][y][int((shape+1)%2)]:
                    visit[x+1][y][int((shape+1)%2)] = True
                    q.append([[x+1,y],[int((shape+1)%2),cnt+1]])
                    
            if x-1>=0 and y-1>=0 and board[x-1][y] == 0 and board[x-1][y-1] == 0:
                if not visit[x][y-1][int((shape+1)%2)]:
                    visit[x][y-1][int((shape+1)%2)] = True
                    q.append([[x,y-1],[int((shape+1)%2),cnt+1]])
                    
                if not visit[x][y][int((shape+1)%2)]:
                    visit[x][y][int((shape+1)%2)] = True
                    q.append([[x,y],[int((shape+1)%2),cnt+1]])
        
        else:
            #오른쪽
            if x-1>=0 and y+1<N and board[x][y+1] == 0 and board[x-1][y+1] ==0:
                if not visit[x][y+1][shape]:
                    visit[x][y+1][shape] = True
                    q.append([[x,y+1],[shape,cnt+1]])
            #왼쪽
            if x-1>=0 and y-1>=0 and board[x][y-1] == 0 and board[x-1][y-1] ==0:
                if not visit[x][y-1][shape]:
                    visit[x][y-1][shape] = True
                    q.append([[x,y-1],[shape,cnt+1]])
            #아래
            if x+1<N and board[x+1][y] == 0:
                if not visit[x+1][y][shape]:
                    visit[x+1][y][shape] = True
                    q.append([[x+1,y],[shape,cnt+1]])
            #위
            if x-2>=0 and board[x-2][y] == 0:
                if not visit[x-1][y][shape]:
                    visit[x-1][y][shape] = True
                    q.append([[x-1,y],[shape,cnt+1]])
            #회전
            if x-1>=0 and y+1<N and board[x][y+1] == 0 and board[x-1][y+1] == 0:
                if not visit[x-1][y+1][int((shape+1)%2)]:
                    visit[x-1][y+1][int((shape+1)%2)] = True
                    q.append([[x-1,y+1],[int((shape+1)%2),cnt+1]])
                    
                if not visit[x][y+1][int((shape+1)%2)]:
                    visit[x][y+1][int((shape+1)%2)] = True
                    q.append([[x,y+1],[int((shape+1)%2),cnt+1]])
                    
            if x-1>=0 and y-1>=0 and board[x][y-1] == 0 and board[x-1][y-1] == 0:
                if not visit[x-1][y][int((shape+1)%2)]:
                    visit[x-1][y][int((shape+1)%2)] = True
                    q.append([[x-1,y],[int((shape+1)%2),cnt+1]])
                if not visit[x][y][int((shape+1)%2)]:
                    visit[x][y][int((shape+1)%2)] = True
                    q.append([[x,y],[int((shape+1)%2),cnt+1]])
        
    





print(solution([[0,0,0,1,1],[0,0,0,1,0],[0,1,0,1,1],[1,1,0,0,1],[0,0,0,0,0]]))


#움직일 대상이 2칸을 차지하는 것과 이것을 어떻게 방문처리를 하는지 생각해야 한다 최단거리이므로 BFS를 사용하고 visit를 가로, 세로의 경우 두 가지를 고려해 3차원 배열을 사용한다