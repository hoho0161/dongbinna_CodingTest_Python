
def rotate_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
            
    return result

def check(new_lock):
    lock_len = len(new_lock) // 3
    for i in range(lock_len,lock_len*2):
        for j in range(lock_len,lock_len * 2):
            if new_lock[i][j] != 1:
                return False
                
    return True

def solution(key,lock):
    n = len(lock)
    m = len(key)
    
    new_lock = [[0] * (n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
            
            
    for roatation in range(4):
        key = rotate_90_degree(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                        
                if check(new_lock) == True:
                    return True
                
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
                        
                        
    return False
            
            


    # krots = [
    #     key,                                                                        # 0도, 기본
    #     list(zip(*reversed(key))),                                                  #90도, 회전
    #     list(map(lambda e:list(reversed(e)), reversed(key))),                       #180도, 회전
    #     list(map(lambda e:list(reversed(e)), reversed(list(zip(*reversed(key)))))), #270도, 회전
    # ]
    
    # 행렬 90도 회전방법, 배열 패딩을 사용하여 자물쇠확인
    