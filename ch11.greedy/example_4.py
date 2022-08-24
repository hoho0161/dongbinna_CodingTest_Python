n = int(input())

data = list(map(int,input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x
    
print(target)

#화폐를 오름차순으로 만들고 목표화폐금액을 만들수 있는지 순서대로 확인해본다
# target+= x 로 만들수있는지 확인하는 금액을 갱신해주고 x가 target보다 크면 못만드는 상황이므로 target을 반환해준다.
