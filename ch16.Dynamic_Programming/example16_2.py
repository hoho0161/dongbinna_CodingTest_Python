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


'''
다른 풀이 - zip를 활용해 계산할 것만 묶어 accum에 dp정보를 계속 갱신해가는 풀이법이다
def solution():
    import sys
    n = int(input())
    triangle =[]
    for _ in range(n):
        triangle.append(list(map(int, sys.stdin.readline().rstrip().split())))
                   
    accum = []
    for i in range(n):
        accum = [max(a+c, b+c) for a,b,c in zip([0]+accum, accum+[0], triangle[i])] #[0]+accum으로 왼쪽위 최대합,accum+[0]로 오른쪽 최대합,자신의수로 한 튜플을 이룸
    print(max(accum))
'''