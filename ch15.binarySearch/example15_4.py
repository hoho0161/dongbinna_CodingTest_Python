from bisect import bisect_left, bisect_right

array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]

def count_by_range(a,left_value,right_value):
    right_idx = bisect_right(a,right_value)
    left_idx = bisect_left(a,left_value)
    return right_idx - left_idx

def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1]) # 역순으로 된 단어 저장
    
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()
        
    for q in queries:
        if q[0] != '?':
            res = count_by_range(array[len(q)],q.replace('?','a'),q.replace('?','z'))
        else:
            res = count_by_range(reversed_array[len(q)],q[::-1].replace('?','a'),q[::-1].replace('?','z'))
        
        answer.append(res)    
    return answer


# string의 sort의 경우 아스키코드대로 대문자 -> 소문자 a->z 순으로 정렬된다
# 배열의 index에 접근하는 방법을 extended slices 라고 부른다 [::-1]의 경우 처음부터 끝까지 -1칸 간격으로 => 역순이란 뜻이다