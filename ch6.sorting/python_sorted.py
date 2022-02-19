array = [7,5,9,0,3,1,6,2,4,8]

result = sorted(array)
print(result)

#내부 원소를 바로 정렬가능
array.sort()
print(array)

#key 매개변수를 입력으로 받을 수 있다

array = [('바나나',2),('사과',5),('당근',3)]

def setting(data):
    return data[1]

result = sorted(array,key=setting)
print(result)

#람다함수 사용
result1 = sorted(array,key=lambda data: data[1])
print(result)