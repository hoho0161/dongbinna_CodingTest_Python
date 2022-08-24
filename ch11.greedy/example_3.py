s = input()
s = list(s)

count = 0
count1 = 0
ch = False
ch1 = False

for i in s:
    if i =='0':
        if ch == True:
            count+=1
            ch = False
        if ch1 == False:
            ch1 = True
    elif i == '1':
        if ch == False:
            ch = True
        if ch1 == True:
            count1 += 1
            ch1 = False
        
if ch == True:
    count+=1

if ch1 == True:
    count1+=1

res = min(count,count1)
print(res)

# 0과1의 연속된 구간으로 나눠 적은 것을 골랐다