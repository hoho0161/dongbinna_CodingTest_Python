
n,m = map(int,input().split())
array = list(map(int,input().split()))

#인덱스범위 0~최대떡길이
start = 0
end = max(array)

#반복
def binary_search(array, target,start,end):
    result = 0
    
    while start<=end :
        # 자른 떡길이 값의합
        total = 0
        mid = (start+end) // 2
        for x in array:
            if x > mid:
                total += x - mid
        
        #떡길이가 모자르면 end 조정
        if total < target:
            end = mid - 1
        #길이가 충분하면 절단기 높이를 높여 최댓값이 있는지 확인하기
        else:
            result = mid
            start = mid + 1
    
    return result

print(binary_search(array,m,start,end))


#전형적인 이진 탐색문제, 파라메트릭 서치 유형의 문제  -  최적화문제를 결정(yes or no) 문제로 바꾸어 해결함