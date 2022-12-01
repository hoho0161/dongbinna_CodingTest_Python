n = int(input())
data = []

for i in range(n):
    data.append(list(map(int,input().split())))
    
dp = [0]*(n+1)

for i in range(n+1):
    for j in range(i):
        if j + data[j][0] <= i:
            dp[i] = max(dp[i],dp[j] + data[j][1])
            
print(dp[n])

# dp 테이블에 각 날짜까지 얻을수 있는 최대 보수(당일제외)를 저장한다
# 그후 전날들의 날짜(j)와 걸리는상담시간(data[j][1])을 더해 해당날짜전에 완료가능하면 전날 날짜의 DP테이블값과 해당날짜상담 보수를 더해 최대값을 비교 후 갱신해준다 