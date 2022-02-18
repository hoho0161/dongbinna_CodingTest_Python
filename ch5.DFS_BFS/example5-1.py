#DFS 문제

n,m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input())))
    

    
def countIcecream(graph,x,y):
    
    #초기조건1 인덱스오류일시
    if x < 0 or x > n-1 or y < 0 or y > m-1:
        return False
    
    #방문하지 않은 곳이면 방문하기
    if graph[x][y] == 0:
        graph[x][y] = 1
        
        #방문후 상하좌우에 빈곳이 있는지 확인하기
        countIcecream(graph,x-1,y)
        countIcecream(graph,x+1,y)
        countIcecream(graph,x,y-1)
        countIcecream(graph,x,y+1)
        
        #방문 후 아이스크림 개수추가를 위한 True 반환
        return True
    
    #방문한 곳이면 False반환
    return False
        
        
result = 0

for i in range(n):
    for j in range(m):
        if countIcecream(graph,i,j) == True:
            result += 1

print(result)