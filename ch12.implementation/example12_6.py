def possible(answer):
    for x,y, stuff in answer:
        if stuff == 0:
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False
        elif stuff == 1:
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
    
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x,y,stuff,operate = frame
        if operate == 0:
            answer.remove([x,y,stuff])
            if not possible(answer):
                answer.append([x,y,stuff])
        if operate == 1:
            answer.append([x,y,stuff])
            if not possible(answer):
                answer.remove([x,y,stuff])
    
    return sorted(answer)
                
                
# 일반적인 구현문제 설치제거후 answer값을 넘겨 존재가능한가를 함수로 만들어 풀수있다
# sorted(answer) 같은 경우 key=itemgetter(parameter) 에 parameter 값을 리스트 크기만큼(ex itemgetter(0,1,2)) 인덱스로 전부 넘겼을 때와 같은 값이 나왔다