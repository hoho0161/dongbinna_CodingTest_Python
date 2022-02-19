array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x<= pivot] #분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] #분할된 오른쪽 부분
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))

#퀵 정렬 시간복잡도 : 평균 O(NlogN) - 최악의 경우 O(N^2) 데이터를 피벗으로 삼을 때 '이미 데이터가 정렬되어 있는 경우'에는 매우 느리게 작동
# 퀵기반 정렬라이브러리는 O(NlogN)이 되는 것을 보장할 수 있도록 피벗값을 설정할 때 추가적인 로직을 더해준다.

