n = int(input())
data = input().split()

move = ['U','D','L','R']
#UDLR 순서
dx = [-1,1,0,0]
dy = [0,0,-1,1]


#x,y
x = 1
y = 1

for i in range(len(data)):
    for j in range(len(move)):
        if move[j] == data[i]:
            next_x = x + dx[j]
            next_y = y + dy[j]
            break
    if next_x < 1 or next_x > n or next_y < 1 or next_y > n:
        continue
    
    x,y = next_x,next_y
    
print(x,y)