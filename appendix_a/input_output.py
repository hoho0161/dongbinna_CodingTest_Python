#입력받을 때 input() 사용 - 한 줄의 문자열 입력
#정수로 바꾸는 int() 사용

#띄어쓰기로 구분하여 각각 정수형 데이터로 저장하는 코드

#데이터개수
n = int(input())
#공백으로 구분하여 입력
data = list(map(int,input().split()))   #중요문법

data.sort(reverse = True)
print(data)

#적은 수 일 경우 입력
n, m, k = map(int, input().split())
print(n,m,k)

##################
#입력의 개수가 많은 경우 함수속도가 느려 시간초과가능 파이썬 sys라이브러리의 sys.stdin.readline()함수 이용한다.
import sys
#readline()으로 입력시 입력 후 엔터가 줄 바꿈 기호로 입력되는데, 이 공백을 제거하려면 rstrip()함수를 사용해야한다.

data = sys.stdin.readline().rstrip()
print(data)


answer = 7

#변수를 문자열로 바꾸어 출력
print("정답은 "+ str(answer) +"입니다.")

#콤마 사용 출력 - 의도치않은 공백삽입
print("정답은",answer,"입니다.")

# f-string 문법
print(f"정답은 {answer}입니다.")