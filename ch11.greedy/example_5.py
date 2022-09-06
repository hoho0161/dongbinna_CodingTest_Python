n,m = map(int,input().split())
d = list(map(int,input().split()))

arr = [0]* 11

for x in d:
    arr[x] += 1
    
res = 0

for i in range(1,m+1):
    n -= arr[i]
    res += arr[i] * n
    
print(res)

#무게순으로 해당무게 가질수있는 수 * 그 무게 보다 높은 개수를 res 에 누적시키며 계산한다