str = input()

summ = 0
li = []

for i in str:
    if i >= '0' and i <= '9':
        summ += int(i)
    else:
        li.append(i)
        
li.sort()

for i in li:
    print(i,end='')
if summ != 0:
    print(summ)