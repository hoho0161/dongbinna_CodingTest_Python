n, m = map(int,input().split())

#화폐가치
array = []

for i in range(n):
    array.append(int(input()))

# 10001 은 구성방법이 존재하지 않을 경우를 위해 사용    
d = [10001] * (m+1)
d[0] = 0 # 0원일때부터 시작

for i in range(n):
    unit = array[i]
    for j in range(unit,m+1):
        if d[j-unit] != 10001:
            d[j] = min(d[j],d[j-unit]+1)
        
    
if d[m] == 10001:
    print(-1)
else:
    print(d[m])