d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3,n+1):
    d[i] = d[i - 1] + d[i - 2]
    
print(d[n])

# 반복문을 이용하여 작은 문제부터 차근차근 답을 도출한다고 하여 bottom-up 방식이라고 말한다.
# 다이나믹 전형적인 형태는 보텀업 방식이다. - 결과 저장용 리스트는 'DP 테이블'이라고 부른다.