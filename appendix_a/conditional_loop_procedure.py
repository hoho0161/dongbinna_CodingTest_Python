#조건문

x = 15
if x >= 10:
    print(x)

#조건문 작성시 들여쓰기로 설정  4개의 공백문자 사용이 사실상의 표준격임

#비교연산자
# X==Y , X!=Y , X>=Y ...

#논리연산자
# X and Y , X or Y , not X

#기타연산자
# X in 리스트           리스트 안에 X가 들어가 있을 때 True
# X not in 문자열       문자열 안에 X가 들어가 있지 않을 때 True


#조건문의 값이 True여도 아무것도 처리하고 싶지 않을 때 pass문 사용
score = 85

if score >= 80:
    pass #나중에 작성할 코드
else:
    print('성적이 80점 미만')
print('프로그램 종료합니다')

#조건문 실행코드가 짧을 경우 줄 바꿈을 하지 않아도 됨

if score >= 80: result = 'Sucess'
else : reuslt = 'Fail'

print(result)

#조건부 표현식

a = [1,2,3,4,5,5]
remove_set = {3,5}

result = [i for i in a if i not in remove_set]
print(result)


#반복문 while이나 for 사용

#while
i = 1
result = 0

while i<=9:
    result += i
    i += 1

print(result)

#for
result = 0

for i in range(1,10):
    result += i

print(result)

#함수

def add(a,b):
    return a+b

print(add(3,7))

#인자를 넘겨줄 때 직접 지정가능

def add2(a,b):
    print('함수의 결과:',a+b)

add2(b = 3,a = 7)

#함수 안에서 함수 밖의 변수 데이터 변경하는 경우 global 키워드 
a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)

# 파이썬에서는 람다 표현식 사용가능  -> 간단한 함수를 한줄에 정의
print("lambda",(lambda a,b: a+ b)(3,7))