def solve():
    from collections import deque
    a,b = map(int,input().split())
    limit = 200001
    board = [0] * limit
    Q = deque()
    
    board[a] = 1
    Q.append(a)
    
    while Q:
        curr_x = Q.popleft()
        
        if curr_x == b:
            print(board[curr_x]-1)
            return
        
        for nx in [curr_x-1,curr_x+1,curr_x*2]:
            # print(nx)
            if nx<0 or nx>= limit:
                continue
            if board[nx] > 0:
                continue
            # print(nx)
            board[nx] = board[curr_x] + 1  
            Q.append(nx)

solve()