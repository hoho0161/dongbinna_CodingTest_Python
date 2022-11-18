import sys
input = sys.stdin.readline

n = int(input())

a = []
for _ in range(n):
    st = input().split()
    st[1] = int(st[1])
    st[2] = int(st[2])
    st[3] = int(st[3])
    a.append(st)
    
a.sort(key=lambda x : x[0])
a.sort(key=lambda x : x[3],reverse = True)
a.sort(key=lambda x : x[2])
a.sort(key=lambda x : x[1],reverse = True)



    
for i in a:
    print(i[0])
    

# sort에 key=lambda x : (-x[1],x[2],-x[3],x[0]) 으로 플러스이면 오름차순 마이너스면 내림차순으로 정렬할 수 있으며 적힌 순서대로 값을 먼저 비교해준다