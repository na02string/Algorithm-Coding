def solution(m, n, puddles):
    answer = 0
    board = [[0]*m for _ in range(n)]
    for i,j in puddles:
        board[j-1][i-1] = -1 # 못지나가는 곳 표시
    
    print(board)
    
    return answer