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