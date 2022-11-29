from bisect import bisect_left, bisect_right

n, x = map(int,input().split())

data = list(map(int,input().split()))

leftidx = bisect_left(data,x)
rightidx = bisect_right(data,x)


res = rightidx - leftidx

if res == 0:
    print(-1)
else:
    print(res)
    

# bisect 사용법 알아두기
# 이진탐색의 경우 정렬된 배열에서 사용하여 O(logN) 시간으로 찾아낼수 있다 선형인 O(N) 보다 빠르게 찾아야 할 경우 필요하다