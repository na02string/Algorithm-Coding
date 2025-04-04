from collections import deque
T = int(input()) # 테스트 케이스 개수
for _ in range(T):
    m,n,k =map(int, input().split()) 
    located = deque() # 배추가 있는 위치
    board = [[-1]*m for _ in range(n)] # n행 m열

    dx = [0,-1,0,1]
    dy = [1,0,-1,0]

    for _ in range(k):
        x,y = map(int,input().split())
        board[y][x] = 0  # 배추가 있으면 0
        located.append((y,x))  # (row, col) = (y,x)

    worm = 0
    Q = deque()
    
    for y,x in located:
        if board[y][x] != 0:
            continue

        worm += 1
        Q.append((y,x))
        board[y][x] = worm
        
        while Q:
            curr_y,curr_x = Q.popleft()

            for i in range(4):
                ny = curr_y + dy[i]
                nx = curr_x + dx[i]

                if ny<0 or ny>=n or nx<0 or nx>=m:
                    continue
                if board[ny][nx] != 0:
                    continue

                board[ny][nx] = worm
                Q.append((ny,nx))
    print(worm)
