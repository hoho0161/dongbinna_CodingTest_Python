test_case = int(input())

for t in range(test_case):
    n, m = map(int,input().split())
    array = list(map(int,input().split()))


    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m
        
    for j in range(1,m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up,left_down,left)
            
    result = 0
    for i in range(n):
        result = max(result,dp[i][m-1])
        
    print(result)
    
# 간단한 dp문제 점화식을 쉽게 떠올릴수 있어 구현만 잘하면 된다