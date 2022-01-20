n = int(input())

ret = 0

for i in range(0,n+1):
    for j in range(0,60):
        for k in range(0,60):
            if str(i).find('3') != -1 or str(j).find('3') != -1 or str(k).find('3') != -1:
                ret += 1
        
print(ret)

## 답안에는 if '3' in str(i)+str(j)+str(k): 로 작성해 문자열을 더한 후 3를 찾는다.