idx = input()

col = ord(idx[0]) - ord('a') #a부터 0으로 
row = int(idx[1]) -1  # 인덱스를 0부터로

dx = [1,1,-1,-1,2,2,-2,-2]
dy = [-2,2,-2,2,-1,1,-1,1]

ret = 0

for i in range(len(dx)):
    if (col+dy[i]) > 7 or (col+dy[i]) < 0 or (row+dx[i]) > 7 or (row+dx[i]) < 0:
        continue
    ret += 1

print(ret)



### 답안의 경우 dx,dy를 steps = [(-2,-1), (-1,-2) ....] 으로 구현해 for step in steps:로 사용했다 2가지 형태 모두 자주 사용되므로 참고하자
#알파벳을 a로부터 떨어진 간격을 센다하면  ord('e') - ord('a') 로  a는 0, b는 1.... 로 매핑가능