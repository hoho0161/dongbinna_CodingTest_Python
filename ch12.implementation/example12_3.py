def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1):
        idx = 0
        result = ""
        while idx < len(s):
            c = s[idx:idx+i]
            n = 1
            while c == s[idx+i:idx+i+i]:
                n += 1
                idx = idx+i
            
            result = result + ((str(n)+c) if n!=1 else c)
            idx = idx+i
        
        answer = min(len(result),answer)
    
    return answer


# 다른 사람의 풀이에서 zip으로 인덱스 s[1:]+[''] 와 함께 묶어 for문으로 같은지 확인하는 방법도 존재하였다.
