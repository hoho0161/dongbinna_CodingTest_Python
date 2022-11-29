import sys

input = sys.stdin.readline

n, c = map(int,input().split())

data = []

for _ in range(n):
    data.append(int(input()))
    
data.sort()

start = 1 #가능 최소 거리
end = data[-1] - data[0] #가능 최대 거리
result = 0


while start <= end:
    mid = (start+end) // 2
    value = data[0]
    count = 1
    for i in range(1,n):
        if data[i] >= value + mid:
            value = data[i]
            count += 1
            
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
        
        
print(result)

# 파라메트릭 서치 유형의 문제이다 정렬된 배열을 가지고 이진탐색을 하는 것이 아닌 
# 최소거리와 최대거리(정렬된 배열 끝-첫값)을 기준으로 이진탐색을 하며 공유기를 충분히 놓을 수 있는지 확인한다

# 정렬된 배열에 이진탐색을 무조건 적용한다는 생각을 고쳐야 한다