import sys

input = sys.stdin.readline

n = int(input())

data = []

for i in range(n):
    data.append(list(map(int,input().split())))
    
dp = [[0]*n for _ in range(n)]
dp[0][0] = data[0][0]

for i in range(1,n):
    for j in range(i+1):
        if j==0:
            left_up = 0
        else:
            left_up = data[i][j] + dp[i-1][j-1]
        
        if j==i:
            right_up = 0
        else:
            right_up = data[i][j] + dp[i-1][j]
            
        dp[i][j] = max(left_up,right_up)
        

print(max(dp[n-1]))