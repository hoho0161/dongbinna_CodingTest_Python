from collections import deque

test_case = int(input())

for case in range(test_case):
    n = int(input())
    last_rank= list(map(int,input().split()))
        
    

    graph =[[False]*(n+1) for _ in range(n+1)]

    indegree = [0] * (n+1)

    for i in range(n):
        for j in range(i+1,n):
            graph[last_rank[i]][last_rank[j]] = True
            indegree[last_rank[j]] += 1
            
    m = int(input())
    
    for _ in range(m):
        t1, t2 = map(int,input().split())
        
        if graph[t1][t2]:
            graph[t1][t2] = False
            graph[t2][t1] = True
            indegree[t1] += 1
            indegree[t2] -= 1
        else:
            graph[t1][t2] = True
            graph[t2][t1] = False
            indegree[t1] -= 1
            indegree[t2] += 1
            
    result = []    
    q = deque()
    
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
            
    certain = True # 정렬결과가 오직 하나인지 확인
    cycle = False # 사이클존재 여부 확인
    
    for i in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            certain = False
            break
    
        now = q.popleft()
        result.append(now)
        
        for j in range(1,n+1):
            if graph[now][j]:
                indegree[j] -= 1
                
                if indegree[j] == 0:
                    q.append(j)
        
    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i, end=' ')
        print() 
                

    # 위상정렬을 사용한다 낮은순위가 높은순위를 가르킨다 순위가 반전되면 그 간선을 반대로 놔주고 1. 사이클 2. 다수결과 3. 1개결과로 구분해준다