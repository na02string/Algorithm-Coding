from collections import deque
def solution(storage, requests):
    answer = 0
    n = len(storage)
    m = len(storage[0])
    
    storage.insert(0,"0"*m)
    storage.append("0"*m)
    board=[]
    for i in storage:
        i = "0"+i+"0"
        board.append(list(i))
    
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    
    for req in requests:
        if len(req) == 1: # 0인 칸 돌아다니면서 0칸 주변에 그 알파벳 잇으면 0으로 변환. 
            visited = [[False]*(m+2) for _ in range(n+2)]
            q = deque()
            q.append((0,0))
            visited [0][0] = True
            
            while q:
                curr_x, curr_y = q.popleft()
                for i in range(4):
                    nx = curr_x + dx[i]
                    ny = curr_y + dy[i]
                    
                    if nx<0 or nx>=(n+2) or ny<0 or ny>=(m+2):
                        continue
                    else:
                        if (board[nx][ny] == "0") and visited[nx][ny] == False:
                            q.append((nx,ny))
                            visited[nx][ny] = True
                        elif board[nx][ny] == req and visited[nx][ny] == False:
                            board[nx][ny] = "0"
                            visited[nx][ny] = True
                        else:
                            continue
        else: # req 에 해당하는 알파벳 다 0으로 바꿈
            for i in range(n+2):
                for j in range(m+2):
                    if board[i][j] == req[0]:
                        board[i][j] = "0"
    for i in range(n+2):
        for j in range(m+2):
            if board[i][j] != "0":
                answer += 1
  

    return answer