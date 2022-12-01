n = int(input())
data = list(map(int,input().split()))

data.reverse()
    
dp = [1]*n

for i in range(1,n):
    for j in range(0,i):
        if data[j] < data[i]:
            dp[i] = max(dp[i],dp[j] + 1)
            
            
print(n - max(dp))

# 가장 긴 증가하는 부분 수열 (LIS, Longest Increasing Subsequence)로 알려진 dp문제 아이디어를 사용한다
# reverse 메서드를 사용해 오름차순으로 바꿔준다
# dp 테이블에는 dp[i]의 경우 data[i]가 마지막 원소로 있을때 최대 길이가 된다
# 가장 긴 수열은 병사가 남아있는 수이므로 총 병사수에서 빼줘 열외해야할 병사 수를 구해준다
# O(n^2)의 알고리즘이며 이진탐색을 활용한 O(n log n)으로 개선할 수 있다 추가적인 테이블이 필요하다