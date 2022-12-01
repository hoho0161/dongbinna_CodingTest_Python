

n = int(input())

q = set()
q.add(1)

cnt = 2
while len(q) < n:
    if cnt%2 == 0:
        if (cnt//2) in q:
            q.add(cnt)
    elif cnt%3 == 0:
        if (cnt//3) in q:
            q.add(cnt)
    elif cnt%5 == 0:
        if (cnt//5) in q:
            q.add(cnt)
    cnt+=1
    
res = list(q)
res.sort()

print(res[n-1])
    
# 책의 해설에서는 dp에 순서대로 못생긴수를 저장한다 정렬을 한번해야하는 내 풀이의 경우 조금 느리게 작돌할것이다