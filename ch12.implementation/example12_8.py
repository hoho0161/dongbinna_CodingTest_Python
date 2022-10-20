from itertools import permutations



def solution(n, weak, dist):
    
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    answer = len(dist)+1 
    
    # 0~ length -1 까지 위치를 각각 시작점으로 설정
    for start in range(length):
        #친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for friends in list(permutations(dist,len(dist))):
            count = 1 #투입할 친구의 수
            position = weak[start] + friends[count -1] 
            #시작점부터 모든 취약지점을 확인
            for index in range(start,start+length):
                # 점검위치를 벗어나는 경우
                if position < weak[index]:
                    count += 1
                    if count > len(dist): # 더 투입 불가능하면 종료
                        break
                    position = weak[index] + friends[count -1] # 점검이 필요한 새친구를 위치에 배치해준다
                    
            answer = min(answer,count)
            
    if answer > len(dist):
        return -1
    return answer

# 제한조건이 매우작아 완전탐색의 가능성을 생각해내야 한다
#  원형으로 나열된 데이터를 처리하는 경우 길이를 2배 늘려서 일자 형태로 만들어 주는 작업을 해주면 유리하다