n = int(input())

d = list(map(int,input().split()))

d.sort()

print(d[(len(d)-1)//2])


# 정렬 후 중간값이 거리가 최소가 된다
# 출력 조건에 설치가 여러대 가능할시 작은값 출력 -> 집이 짝수개이면 중간값 인덱스 2개중 작은거를 골라 출력
