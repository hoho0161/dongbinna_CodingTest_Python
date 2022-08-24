s = input()

li = list(s)
li = list(map(int,li))

res = li[0]
for i in li[1:]:
    if res <=1:
        res += i
    else:
        if i <= 1:
            res += i
        else:
            res *= i
            
print(res)

# 곱할때 피연산자 둘다 1이하이면 더하기 아니면 곱하기