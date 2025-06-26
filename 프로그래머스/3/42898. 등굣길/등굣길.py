def solution(m, n, puddles):
    board = [[0]*m for _ in range(n)]
    for i,j in puddles:
        board[j-1][i-1] = -1 # 못지나가는 곳 -1로 표시
    count = [[0]*m for _ in range(n)] # 최단 경로 횟수
    dx = [1,0]
    dy = [0,1]
    
    from collections import deque
    q = deque()
    q.append((0,0))
    board[0][0] = 1 # 이동 거리
    count[0][0] = 1
    
    while q:
        curr_x, curr_y = q.popleft()
        
        for i in range(2):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]
            
            if nx >= n or ny >= m: # out of range
                continue
            if board[nx][ny] == -1: # 갈수 없는 경우 패스
                continue
            if board[nx][ny] == 0: # 방문한적 없는 위치인경우
                board[nx][ny] = board[curr_x][curr_y] + 1 # 그 위치로 가는 최단 경로 기록
                count[nx][ny] = count[curr_x][curr_y]
                q.append((nx,ny))
                
            else:
                # 이제는 이미 최단 경로로 방문한적 있는경우
                # 이때는 이번에 방문한게 최단 경로인지 아닌지 체크해서 count를 올릴지 말지를 결정
                if (board[curr_x][curr_y] + 1) == board[nx][ny]:
                    count[nx][ny] += count[curr_x][curr_y]
    # print(board)
    # print(count)
    return count[n-1][m-1]%1000000007