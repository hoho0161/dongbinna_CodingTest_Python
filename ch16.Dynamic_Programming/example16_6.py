a = input()
b = input()

al = len(a)
bl = len(b)

dp = [[0] * (bl+1) for _ in range(al+1)]

for i in range(1,al+1):
    dp[i][0] = i
for j in range(1,bl+1):
    dp[0][j] = j
    
for i in range(1,al+1):
    for j in range(1,bl+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1 + min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
            
print(dp[al][bl])
    
# 편집거리 알고리즘이다 분명히 기억상으로는 풀이를 본적이 있었는데 잊어버린거 같다.
# 각 문자열의 접두사부분을 최소편집거리로 수정할 수 있는 dp테이블을 만든다 dp[3][2]은 a[:3]에서 b[:2]로 변하는데 필요한 최소 편집거리가 저장된다
# 점화식은 두 문자가 같은경우 dp[i][j] = dp[i-1][j-1] 이고 다른경우 dp[i][j] = 1 + min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]) 이 된다