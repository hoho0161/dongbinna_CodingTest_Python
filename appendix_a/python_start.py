#리스트를 초기화하는 방법 중 하나이다. 대괄호안에 조건문과 반복문을 넣는 방식

#ex1
array = [i for i in range(20) if i % 2 == 1]
print("컴프리헨션 초기화1: ",array)

#ex2
array = [i * i for i in range(1,10)]
print("컴프리헨션 초기화2: ",array)

#ex3  2차원배열 초기화 (컴프리헨션)
n = 3
m = 4
array = [[0] * m for _ in range(n)] # 언더바(_)는 반복을 위한 변수의 값을 무시하고자 할 때
print("컴프리헨션2차원: ",array)


# 잘못된 2차원 배열 초기화
n = 3
m = 4
array = [[0] * m] * n
print("wrong example",array)

array[1][1] = 5  
print("wrong example",array)

#리스트 관련 메서드

a = [1,4,3]
print("기본 리스트", a)

#원소삽입
a.append(2)
print("삽입: ", a)

#오름차순 정렬
a.sort()
print("오름차순: ",a)

#내림차순 정렬
a.sort(reverse=True)
print("내림차순: ",a)

#리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기: ",a)

#특정 인덱스에 추가
a.insert(2,3)
print("인덱스 2에 3추가: ",a)

#특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수: ", a.count(3))

#특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제: ", a)

#insert함수는 시간복잡도 O(n)이다. append함수는 O(1)이다. 추가로 remove함수 또한 O(n)이다.

#remove_all 기본제공을 하지 않으므로 구현법
a = [1,2,3,4,5,5,5]
remove_set = {3,5}
print("before remove_all: ",a);

#remove_set에 포함되지 않는 값만을 저장
result = [i for i in a if i not in remove_set]
print("remove_all: ",result)

print()

#문자열 따옴표로 초기화를 한다
data = 'Hello World'
print(data)

# 백슬래시를 사용하면 큰따옴표나 작은따옴표를 원하는 만큼  포함가능
data = "Don't you know \"Python\""
print(data)

#문자열 연산
a = "Hello"
b = "World"

print(a + " " + b)

a = "String"
print(a*3)

#파이썬의 문자열은 내부적으로 리스트와 같이 처리
a = "ABCDEF"
print(a[2:4])

#튜플 자료형

#리스트와 거의 비슷한데 차이점이 존재
#튜플은 한 번 선언된 값을 변경할 수 없다.
#튜플은 소괄호를 이용한다.

a = (1,2,3,4)
print("튜플: ",a)

#a[2] = 7   tuple object does not support item assignmet

#튜플은 그래프 알고리즘에서 자주 사용 , 각 원소가 서로 다를 떄 주로 사용


#사전 (키,값)의 쌍을 가지는 자료형 내부적으로 해시 테이블을 이용한다.

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'banana'
data['코코넛'] = 'Coconut'

print("사전: ",data)

# 특정한 원소가 있는지 '원소 in 사전' 형태 사용
if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

#키 데이터만 담은 리스트
key_list = data.keys()
#값 데이터만 담은 리스트
value_list = data.values()

print("key_list: ",key_list)
print("key_value: ",value_list)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])

#집합  중복허락x 순서x -> 인덱싱으로 값을 얻을 수 없다.

data = set([1,1,2,3,4,4,5])
print("set: ",data)

#집합의 중괄호 초기화
data = {1,1,2,3,4,4,5}
print("set: ",data)

#집합 연산

a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

print(a | b) #합집합
print(a & b) #교집합
print(a - b) #차집합

#집합 함수
data = set([1,2,3])
print(data)

#새로운 원소 추가
data.add(4)
print("add: ",data)

#새로운 원소 여러개 추가
data.update([5,6])
print("update: ",data)

#특정한 값 삭제
data.remove(3)
print("remove",data)

