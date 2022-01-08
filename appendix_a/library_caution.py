#표준라이브러리 - 자주사용되는 표준 소스코드를 미리 구현해 놓은 라이브러리
# C++STL 같은 라이브러리
# 이 책에서 설명하는 6가지 정도
# 내장 함수, itertools(반복되는 형태 데이터 처리), heapq(힙 기능 제공, 우선순위 큐 기능), bisect(이진 탐색 기능), collections(덱,카운터 등 자료구조), math(수학 기능)

############### 내장함수
#별도 import 없이 바로 사용할 수 있는 내장함수

#sum - iterable 객체가 입력일때 합을 반환
result = sum([1,2,3,4,5])
print(result)

#min - 작은 값 반환 max - 큰 값 반환
result = min(7,3,5,2)
print(result)
result = max(7,3,5,2)
print(result)

#eval() - 수학수식이 문자열 형식으로 들어오면 수식 계산한 결과를 반환
result = eval("(3+5)*7")
print(result)

#sorted() - iterable 객체가 들어왔을 때 정렬된 결과 
result = sorted([9,1,8,5,4]) #오름차순
print(result)
result = sorted([9,1,8,5,4],reverse=True) #내림차순
print(result)

#특정한 기준에 따라서 정렬 수행
result = sorted([('홍길동',35),('이순신',75),('아무개',50)], key = lambda x:x[1],reverse=True)
print(result)

# iterable 객체는 sort()함수 내장으로 객체 내부 값이 정렬된 값으로 바로 변경된다.
data = [9,1,8,5,4]
data.sort()
print(data)

print()
############### itertools
# 유용한 클래스는 permutations, combinations 이다.

#permutations
from itertools import permutations

data = ['A','B','C']
result = list(permutations(data,3)) #모든 순열
print(result)

#combinations
from itertools import combinations
result = list(combinations(data,2)) #2개를 뽑는 모든 조합
print(result)

#product - 중복해서 순열계산
from itertools import product
result = list(product(data,repeat=2)) #2개를 뽑는 모든 순열(중복허용)
print(result)

#combinations_with_replacement - 중복해서 조합계산
from itertools import combinations_with_replacement
result = list(combinations_with_replacement(data,2))
print(result)

print()
############### heapq
#최단 경로 알고리즘을 포함해 우선순위 큐 기능 구현하고자 할 때 사용
import heapq


#최소힙
def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h,value)
    
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

#최대힙
def heapsort2(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h,-value) # 마이너스를 붙여 임시 변경
    
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort2([1,3,5,7,9,2,4,6,8,0])
print(result)

print()
############### bisect
#이진 탐색을 쉽게 구현 - 정렬된 배열에서 특정한 원소를 찾아야 효과적
#bisect_left, bisect_right함수가 중료 O(logN)

from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
x = 4

print(bisect_left(a,x))
print(bisect_right(a,x))

# left_value <= x <= right_value인 원소개수를 빠르게 계산할 수 있다.
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)
    return right_index - left_index

a = [1,2,3,3,3,3,4,4,8,9]
print(count_by_range(a,4,4))
print(count_by_range(a,-1,3))

print()
############### collections
#유용한 deque 와 counter

#                 리스트 vs deque   deque는 인덱싱,슬라이싱 불가능
#가장 앞에 원소추가 O(N)      O(1)
#가장 뒤에 원소추가 O(1)      O(1)
#가장 앞의 원소제거 O(N)      O(1)
#가장 뒤의 원수제거 O(1)      O(1)

#첫번째에 원소 추가 제거 appendleft(x), popleft()
#마지막에 원소 추가 제거 append(x), pop()

from collections import deque

data = deque([2,3,4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))

#Counter  등장횟수를 세는 기능 제공

from collections import Counter

counter = Counter(['red','blue','red','green','blue','blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))

print()
############### math
#자주 사용되는 수학저인 기능을 포함하고 있는 라이브러리이다.

import math

print(math.factorial(5))
print(math.sqrt(7))
print(math.gcd(21,14))
print(math.pi,math.e)