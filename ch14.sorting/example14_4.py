import sys
import heapq

input = sys.stdin.readline

n = int(input())

data = []
for _ in range(n):
    heapq.heappush(data,int(input()))
    
res = 0

while len(data) != 1: # 1개인 경우 모든 카드가 합쳐져 있다
    one = heapq.heappop(data)
    two = heapq.heappop(data)
    
    sum_value = one + two
    res += sum_value
    heapq.heappush(data,sum_value)
    
print(res)

# 합친뒤에 다시 정렬해줘서 최소값 2개를 이용한다는 것을 기억하자
# 자주 정렬해야 할 경우 힙을 고려해야 하는 것을 기억할 것
