n = int(input())

array = list(map(int,input().split()))

d = [0] * 100

# 0에서 선택 경우
d[0] = array[0]
# 1에서 선택 경우
d[1] = max(array[0],array[1])

# 2부터 n-1 까지 최대값이 되게 하는 점화식
for i in range(2,n):
    d[i] = max(d[i-1],d[i-2]+array[i])
    
print(d[n-1])    
    
    
