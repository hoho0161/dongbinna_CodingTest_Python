#리스트를 초기화하는 방법 중 하나이다. 대괄호안에 조건문과 반복문을 넣는 방식

#ex1
array = [i for i in range(20) if i % 2 == 1]
print(array)

#ex2
array = [i * i for i in range(1,10)]
print(array)

#ex3  2차원배열 초기화 (컴프리헨션)
n = 3
m = 4
array = [[0] * m for _ in range(n)] # 언더바(_)는 반복을 위한 변수의 값을 무시하고자 할 때
print(array)


# 잘못된 2차원 배열 초기화
n = 3
m = 4
array = [[0] * m] * n
print("wrong example",array)

array[1][1] = 5  
print("wrong example",array)

#