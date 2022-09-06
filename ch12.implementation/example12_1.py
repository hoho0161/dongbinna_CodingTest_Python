n = input()

a = list(map(int,n[0:int(len(n)/2)]))
b = list(map(int,n[int(len(n)/2):]))

sum_a = sum(a)
sum_b = sum(b)

if(sum_a==sum_b):
    print("LUCKY")
else:
    print("READY")
    
    
# 책풀이 문자열 길이 절반만큼 int형변환후 sum에 더하고 그후 길이는 빼주어서 0인경우 lucky 출력
