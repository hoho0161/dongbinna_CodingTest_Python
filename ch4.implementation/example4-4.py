n,m = map(int,input().split())
x,y,direction = map(int,input().split())

#방문한칸수
count = 0

#북동남서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

visited = [[0]*m for _ in range(n)]

array = []
for i in range(n):
    array.append(list(map(int,input().split())))

#처음 좌표일때 값 설정
visited[x][y] = 1
count += 1
tosearch = direction

while True:
    #왼쪽이 갈수있는가
    tosearch = ((tosearch-1)+4)%4

    if array[x+dx[tosearch]][y+dy[tosearch]] == 1 or visited[x+dx[tosearch]][y+dy[tosearch]] == 1:
        #4방향 갈곳없으면 뒤로 돌아가기
        if tosearch == direction:
            x = x+dx[((direction-2)+4)%4]
            y = y+dy[((direction-2)+4)%4]
            #바다이면 종료
            if array[x][y] == 1:
                break
        continue
    # 갈수있으면 회전하기
    direction = tosearch
    count += 1
    # 이동하기
    x = x+dx[direction]
    y = y+dy[direction]
    #이동한거 체크하기
    visited[x][y] = 1
    
    
print(count)


### 답안의 경우 turn_time 변수로 방향확인이 4번 일어났는지 확인한다. 
# 또한 회전은 함수로 따로 정의해 global 키워드를 사용하였다. 참고하자