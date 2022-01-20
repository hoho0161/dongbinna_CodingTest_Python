n,k = map(int,input().split())

result = 0

while n!=1:
    if n%k == 0:
        n = n//k
        result += 1
        continue
    n -= 1
    result += 1
    
print(result)


### 내 생각 - 답안에서처럼 n<k 인경우는 if절을 사용하지않는 반복문을 따로 작성 할 수도 있다.

### 효율적인 작성 
# n==k로 나누어떨이지는 수가 될 때 까지 1씩 뺀 후 K로 나누기 if(n<k) 일때까지
# 남은 수는 n-1 번씩 1로 빼므로 result +=(n-1)