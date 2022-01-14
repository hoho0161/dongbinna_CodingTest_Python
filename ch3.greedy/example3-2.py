n, m, k = map(int,input().split())

data = list(map(int,input().split()))

relsut = 0
#데이터 정렬
data.sort()

num1 = data[-1] #가장큰 수 
num2 = data[-2] #두번째 큰 수

count = 0
for i in range(m):
    if count == k:
        relsut += num2
        count = 0
        continue
    relsut += num1
    count += 1
    
print(sum)


#input output
#in : 5 8 3
#     2 4 5 4 6
#out : 46

###### 효율적으로 문제 해결하기  (M의 크기가 100억 이상이면 시간초과가 될것이다)

# 이 문제를 풀려면 가장 먼저 반복되는 수열에 대해서 파악한다   (6+6+6+5) + (6+6+6+5) + ...
# 반복되는 수열의 길이는 K+1이 되므로 M 을 K+1로 나눈 몫이 수열이 반복되는 횟수이다.
# 나누어 떨어지지 않는 경우라면 나머지만큼 큰수가 더해지므로

# count = int(M/(k+1)) * K + M % (K+1)  '가장 큰 수가 더해지는 횟수' 이면
# m - count 는 두번재 큰 수가 더해지는 횟수 이다.


### 내생각 - 반복적으로 등장하는 패턴이 있는지 확인하기, 각각의 횟수들을 수식화 가능한지 살펴보기