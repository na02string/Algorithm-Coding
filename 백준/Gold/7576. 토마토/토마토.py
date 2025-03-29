# 7576 토마토
from collections import deque

m,n = map(int, input().split())
# 익은 토마토(1), 안익은 토마토(0), 토마토 없음(-1)
# 모든 토마토가 익지는 못함 -> -1 출력 / 
# 처음부터 전부 다 익어 있으면(0이 하나도 없으면) -> 0 출력

# board를 만들때 1이 있는 위치를 먼저 뽑아두기
board = []
visited = [[False]*m for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

# 익은 토마토의 위치
ripe_tomato = deque() 
# 처음부터 1인거 넣어서 시작. 평소 Q = deque()를 이걸로 대체

# 안익은 토마토(0) 개수 체크 -> 처음부터 하나도 없으면 바로 0 출력
unripe_tomate = 0

for i in range(n):
    append_list = list(map(int, input().split()))
    board.append(append_list)
    
    unripe_tomate += append_list.count(0)
    
    if append_list.count(1) != 0: # 익은 토마토가 있으면
        for ind, j in enumerate(append_list):
            if j == 1:
                ripe_tomato.append((i,ind))
                visited[i][ind] = True

# 처음부터 익을 토마토가 없으면 0출력
if unripe_tomate == 0:
    print(0)
else:
    while ripe_tomato:
        curr_x, curr_y = ripe_tomato.popleft()
        
        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]

            if nx <0 or nx>=n or ny<0 or ny>=m:
                continue
            if visited[nx][ny] == True or board[nx][ny] == -1:  
                continue
            
            ripe_tomato.append((nx,ny))
            visited[nx][ny] = True
            board[nx][ny] = board[curr_x][curr_y] + 1

    count_zero = False
    max_num = 1
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                count_zero = True
                break
        if count_zero:
            break
        else:
            max_board = max(board[i])
            if max_board > max_num:
                max_num = max_board
    if count_zero:
        print(-1)
    elif max_num != 1:
        print(max_num-1)