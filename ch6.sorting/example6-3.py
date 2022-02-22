n , k = map(int,input().split())


array_a = list(map(int,input().split()))
array_b = list(map(int,input().split()))
    
    
array_a.sort()
array_b.sort(reverse=True)


for i in range(0,k):
    if array_a[i] > array_b[i]:
        continue
    array_a[i] , array_b[i] =  array_b[i] , array_a[i] #스와프
    
    
print(sum(array_a))