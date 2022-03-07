
# find 함수의 O(V) 의 시간복잡도로  전체 알고리즘 O(VM) (M-find,union 수) 가 되어 비효율적이 됨 이를 해결하기 위해 경로압축 기법을 적용한다.
# 경로압축기법 - find 함수를 재귀적으로 호출한 뒤에 부모 테이블값을 갱신하는 기법

def find_parent_compression(parent,x):
    if parent[x] != x:
        parent[x] = find_parent_compression(parent,parent[x])
    return parent[x]

def find_parent(parent,i):
    if parent[i] != i:
        return find_parent(parent,parent[i])
    return i

def union_parent(parent, a, b):
    a = find_parent_compression(parent,a)
    b = find_parent_compression(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    



v, e = map(int,input().split())
parent = [0] * (v+1)

for i in range(1,v+1):
    parent[i] = i
    
for i in range(e):
    a, b = map(int,input().split())
    union_parent(parent,a,b)
    
print('각 원소가 속한 집합: ', end='')
for i in range(1,v+1):
    print(find_parent_compression(parent,i), end=' ')

print()

print('부모 테이블: ', end='')
for i in range(1,v+1):
    print(parent[i], end=' ')
    
    

#서로소 집합 알고리즘 시간복잡도 -  노드최대 V개 find,union 최대 V-1개 가능할 때 경로압축방식적용 알고리즘은 O(V+M(1+log_[2-M/V](V))) 이다

# 추가적으로  최악경우 복잡도는 유지하면서 실제 더 효율적인 한 경로(one-pass) find method 가 존재한다.