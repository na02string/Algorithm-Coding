# bfs로 거리를 측정할 수 있다
from collections import deque

n,m = map(int, input().split())

board = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

Q = deque()
Q.append((0,0))
board[0][0] = 1

while Q:
    curr_x, curr_y = Q.popleft()
    visited[curr_x][curr_y] = True
    
    for i in range(4):
        nx = curr_x + dx[i]
        ny = curr_y + dy[i]
        
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        
        if board[nx][ny] == 0 or visited[nx][ny]==True:
            # 갈 수 없는 0이거나 방문한경우 
            continue
        
        board[nx][ny] = board[curr_x][curr_y] + 1
        visited[nx][ny] = True
        
        Q.append((nx,ny))
    
print(board[n-1][m-1])
