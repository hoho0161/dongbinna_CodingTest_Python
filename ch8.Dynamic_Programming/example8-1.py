n = int(input())

d = [0] * 30001

for i in range(2,n+1):
    #현재 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1
    # 2로 나눠짐
    if i % 2 == 0:
        d[i] = min(d[i],d[i//2] + 1)
    # 3로 나눠짐
    if i % 3 == 0:
        d[i] = min(d[i],d[i//3] + 1)
    # 5로 나눠짐
    if i % 5 == 0:
        d[i] = min(d[i],d[i//5] + 1)
    
    
print(d[n])

# d 리스트는 해당 인덱스숫자가 1이 되기까지 최소연산횟수를 저장해 놓는다.