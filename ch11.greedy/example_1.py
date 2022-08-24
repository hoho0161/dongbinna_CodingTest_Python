n = int(input())

a = list(map(int,input().split()))
a.sort()

count =0
res = 0

for i in a:
    count += 1 #그룹인원
    if count >= i:
        res += 1
        count = 0
        
        
print(res)

#오름차순으로 정렬해 공포심이 적은순으로 그룹을 하여 최대그룹수를 만들어낸다