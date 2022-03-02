d = [0] * 201

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    
    d[x] = fibo(x-2) + fibo(x-1)
    return d[x]


print(fibo(10))

# 재귀함수를 이용하여 큰 문제를 해결하기 위해 작은 문제를 호출하는 방법을 top-down 방식이라고 말한다.