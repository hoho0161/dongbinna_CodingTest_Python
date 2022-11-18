def solution(N, stages):
    a = [0]*(N+2)
    result = []
    p = len(stages)
    
    for i in range(len(stages)):
        a[stages[i]] += 1
        
    for j in range(1,N+1):
        if p == 0:
            result.append((j,0))
            continue
        result.append((j,a[j]/p))
        p -= a[j]
        
    result.sort(key = lambda x: (-x[1],x[0]))
    
    answer = []
    
    for i in result:
        answer.append(i[0])
        
    return answer

print(solution(5,[2,1,2,6,2,4,3,3]))
print(solution(4,[4,4,4,4,4]))
print(solution(5,[3,3,3,3]))