#스택
#파이썬에서는 리스트에서 append() 와 pop()을 사용하여 구현한다.

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])


#큐
# collections 모듈에서 제공하는 deque 자료구조를 활용한다.

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(list(queue)) #자료형을 리스트로 바꿀때

#재귀함수
# 재귀함수 수행은 스택 자료구조를 이용한다

def recursive_function(i):
    if i == 100:
        return
    print(i, '번째 재귀 함수에서', i+1,'번째 재귀 함수를 호출합니다.')
    recursive_function(i+1)
    print(i,'번째 재귀 함수를 종료합니다.')
    
recursive_function(1)


#팩토리얼

#반복적 구현
def factorial_iterative(n):
    result = 1
    # 1~n까지 곱하기
    for i in range(1,n+1,1):
        result *= i
    return result

def factorial_recursive(n):
    if n<=1:
        return 1
    return n * factorial_recursive(n-1)
 
print('반복 :', factorial_iterative(5))
print('재귀 :', factorial_recursive(5))