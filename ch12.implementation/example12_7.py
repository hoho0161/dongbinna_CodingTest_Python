from itertools import combinations

city = []
n,m = map(int,input().split())
for i in range(n):
    li = list(map(int,input().split(' ')))
    city.append(li)

chicken = []
house = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append((i,j))
        if city[i][j] == 1:
            house.append((i,j))
            
picks = list(combinations(chicken,m))

#print(picks)

result = 987654321
for pick in picks:
    s = 0
    for h in house:
        min_dist = 987654321
        for c in pick:
            dist = abs(c[0]-h[0]) + abs(c[1]-h[1])
            if dist < min_dist:
                min_dist = dist
        
        s += min_dist
    
    if s < result:
        result = s
    
print(result)

