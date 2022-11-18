

def decom(text):
    a = []
    b = []
    n1 = 0
    n2 = 0
    
    for i in range(len(text)):
        if text[i] == '(':
            n1+=1
        elif text[i] == ')':
            n2+=1
        
        if n1 == n2:
            a = text[:i+1]
            b = text[i+1:]
            break
    
    return a,b
    

def isRight(text):
    if text == "":
        return True
    
    a = []
    for i in text:
        if i == '(':
            a.append('(')
        elif i == ')':
            if len(a) > 0:
                ch = a.pop()
                if ch == '(':
                    continue
                else:
                    return False
            else:
                return False
    
    if len(a) > 0:
        return False
    else:
        return True
    
def reviseText(text):
    if text == "":
        return text
    
    u, v = decom(text)
    
    if isRight(u):
        return u + reviseText(v)
    else:
        a = '('+reviseText(v)+')'
        b = u[1:-1]
        c = ""
        for i in b:
            if i == '(':
                c += ')'
            elif i == ')':
                c += '('
        a = a+c
        return a
        
        

def solution(p):
    if p== '':
        return p
    
    return reviseText(p)
        
    
print(solution("()))((()"))

#DFS기반 구현문제로 문제에 적힌 구현방법을 정확히 인지해야 하는것을 알았다 4번 변환법을 대충읽고 구현해서 늦었다