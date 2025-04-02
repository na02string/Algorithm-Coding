from collections import deque

R,C = map(int,input().split())
board = [list(input().strip()) for _ in range(R)]

F_time = [[-1]*C for _ in range(R)] # 불이 옮겨간 시간
J_time = [[-1]*C for _ in range(R)] # 지훈이가 옮겨간 시간

J_Q = deque()
F_Q = deque()
        
dx = [1,0,-1,0]
dy = [0,1,0,-1]

# 불의 전파가 되는 시간을 먼저 F_time에 기록하고
# 다음으로 지훈이의 위치를 보는데, 이때 지훈이가 도달하는 시간이 불이 도달한 시간보다 작아야만
# 지훈이가 갈 수 있는길
# 즉,불이 먼저 도달했다면 벽처럼 처리해주기

# 불과 지훈의 시작 위치 deque에 추가
for i in range(R):
    for j in range(C):
        if board[i][j] == 'J':
            J_Q.append((i,j))
            J_time[i][j] = 1
        elif board[i][j] == 'F':
            F_Q.append((i,j))
            F_time[i][j] = 1
# 불 도착 시간 기록
while F_Q:
    curr_x, curr_y = F_Q.popleft()
    
    for i in range(4):
        nx = curr_x + dx[i]
        ny = curr_y + dy[i]
        
        if nx<0 or nx>=R or ny<0 or ny>=C:
            continue
        elif board[nx][ny] == '#' or F_time[nx][ny] != -1:
            continue
        else:
            F_time[nx][ny] = F_time[curr_x][curr_y] + 1
            F_Q.append((nx,ny))

# 지훈이 
def solve():
    while J_Q:
        curr_x, curr_y = J_Q.popleft()
        
        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]
            next_record = J_time[curr_x][curr_y] + 1
            
            if nx<0 or nx >= R or ny<0 or ny >= C:
                print(J_time[curr_x][curr_y])
                return
                
            if board[nx][ny] == '#' or J_time[nx][ny] != -1:
                continue
            # 불이 도착하지 않았거나, 지훈이가 더 빨리 도착하면 이동 가능
            if F_time[nx][ny] != -1 and next_record >= F_time[nx][ny]:
                continue
            J_time[nx][ny] = next_record
            J_Q.append((nx,ny))
    print('IMPOSSIBLE')
    
solve()