def solution(maps):
    # bfs를 이용하면 이동거리를 기록할 수 있음
    n = len(maps)
    m = len(maps[0])
    visited = [[0]*m for _ in range(n)] # 여기에 거리 기록
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    from collections import deque
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    
    while q:
        curr_x, curr_y = q.popleft()
        
        for i in range(4):
            next_x = curr_x + dx[i]
            next_y = curr_y + dy[i]
            
            if next_x >= n or next_x<0 or next_y >= m or next_y<0:
                continue
            if visited[next_x][next_y] != 0 or maps[next_x][next_y] == 0: # 방문한적 있거나 벽이면 못감
                continue
                
            q.append((next_x,next_y)) 
            visited[next_x][next_y] = visited[curr_x][curr_y] + 1
            
    if visited[n-1][m-1] != 0:
        return visited[n-1][m-1]
    else:
        return -1
