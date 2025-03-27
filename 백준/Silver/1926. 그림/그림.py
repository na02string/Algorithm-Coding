from collections import deque
n,m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

visited = [[False]*m for _ in range(n)]   

dx = [1,0,-1,0]
dy = [0,1,0,-1]

total_size = []
num = 0

for i in range(n):
    for j in range(m):
        if visited[i][j] == False and (board[i][j] == 1): 
            # 아직 방문 안한 상태면서 그림인 경우(1인 경우)
            # bfs 탐색의 첫 시발점으로
            Q = deque()
            Q.append((i,j))
            visited[i][j] = True
            size = 1 # 그림 넓이
            num += 1 # 그림 개수
            
            while Q:
                curr_x, curr_y = Q.popleft()
                
                # 범위 초과하지 않는 다음 위치 만들기
                for dir in range(4):
                    nx = curr_x + dx[dir]
                    ny = curr_y + dy[dir]
                
                    if nx <0 or nx >= n or ny <0 or ny >= m:
                        continue
                
                    if board[nx][ny] == 1 and visited[nx][ny] == False: 
                    # 그림 부분이고 거길 방문한적이 없으면
                        Q.append((nx,ny))
                        visited[nx][ny] = True # 방문했다고 체크
                        size += 1
                
            total_size.append(size)

print(num)
if num == 0:
    print(0)
else:
    print(max(total_size))          