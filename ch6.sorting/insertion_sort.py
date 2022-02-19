array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i,0,-1):
        if array[j] < array[j-1]:
            array[j],array[j-1] = array[j-1],array[j]
        else:
            break

print(array)


#데이터가 거의 정렬되어 있는 상태이면 매우 빠르게 동작함
#최선의 경우 O(N)의 시간복잡도를 가짐