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