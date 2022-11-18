
n = int(input())

data = list(map(int,input().split()))

cal = list(map(int,input().split()))

max_res = -1000000001
min_res = 1000000001

def get_result(i,data,cal,res):
    global max_res
    global min_res
    
    #주어진 수 전부계산시 종료
    if i == len(data)-1:
        if max_res < res:
            max_res = res
        if min_res > res:
            min_res = res
            
    for op in range(4):
        if op == 0: # 더하기
            if cal[op] <= 0: #다 사용했으면 다음 연산으로
                continue
            cal[op] -= 1
            get_result(i+1,data,cal,res + data[i+1])
            cal[op] += 1
        if op == 1: # 빼기
            if cal[op] <= 0:
                continue
            cal[op] -= 1
            get_result(i+1,data,cal,res - data[i+1])
            cal[op] += 1
        if op == 2: # 곱하기
            if cal[op] <= 0: #다 사용했으면 다음 연산으로
                continue
            cal[op] -= 1
            get_result(i+1,data,cal,res * data[i+1])
            cal[op] += 1
        if op == 3: # 나누기
            if cal[op] <= 0: #다 사용했으면 다음 연산으로
                continue
            cal[op] -= 1
            get_result(i+1,data,cal,int(res / data[i+1]))
            cal[op] += 1
            
    

get_result(0,data,cal,data[0])
print(max_res)
print(min_res)

# 출력조건에서 최솟값이 -10억인데 초기화때 -1로 해버렸다 조건을 더 꼼꼼히 읽을 수 있도록 하자
# 나눗셈에서 // 쓰면 정답이 안나온다 int(a/b) 이거나 문제에서 주어진대로 양수- abs()로 만들고 나눈뒤 몫만 음수로 바꾸는 방법도 찾을 수 있었다 