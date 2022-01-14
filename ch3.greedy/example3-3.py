n,m = map(int,input().split())

data = [[0]*m for _ in range(n)]

for i in range(n):
    line = list(map(int,input().split()))
    data[i] = line


for i in range(n):
    data[i].sort()

max_in_each_row_value = data[0][0]
for i in range(n):
    if data[i][0] >= max_in_each_row_value:
        max_in_each_row_value = data[i][0]
        
print(max_in_each_row_value)


#답안 비교
### min()함수를 사용하여 각 행마다 최소값을 뽑아내고 그 최소값을 저장해두었던 값과 비교해 그 중 큰값을 뽑는다.


### 내생각 - 데이터를 한번에 저장 후 비교하는 것이 아닌 입력을 받아서 바로바로 확인하는 방법이 있다. 
# 행에서 최소값을 뽑고 다음행에서 비교하여 탐욕법으로 더 큰 수를 선택하면서 또 다시 다음행으로 찾아가는 방법이다.