# 퀸이 공격하는 경우
# 1. 같은 행(row)에 있으면 안 됨
# 3. 같은 열(column)에 있으면 안 됨
# 2. 같은 대각선에 있으면 안 됨

# 백트래킹을 사용해야하는 이유
# 1. 첫 번째 행(0번째 행)에 퀸을 하나 놓는다.
# 2. 다음 행(1번째 행)에 퀸을 놓는데, 첫 번째 퀸과 공격할 수 없는 곳에만 둔다.
# 3. 세 번째 행(2번째 행)도 마찬가지로 안전한 곳을 찾아 퀸을 배치한다.
# 4. 만약 퀸을 놓을 곳이 없다면? 다시 돌아가서(백트래킹) 이전 행의 퀸 위치를 바꿔본다.
def solution(n):
    def is_safe(row, col):
        '''현재 (row, col)에 퀸을 놓을 수 있는 자리인지 확인'''
        for prev_row in range(row):
            prev_col = queen_col[prev_row]
            if (prev_col == col): 
                # row 이전 row들 에서 넣으려는 col에 이미 퀸이 있으면 그자리 못넣음
                return False
            if abs(prev_row - row) == abs(prev_col - col):
                # 대각선 라인에 있어도 못넣음
                return False
            
        # 위 조건에서 모두 살아남은 애들만 넣을 수 있음
        return True
    
    def backtrack(row):
        # 종료조건
        if row == n:
            solutions[0] +=1
            return
        
        for col in range(n):
            if is_safe(row,col):
                queen_col[row] = col
                backtrack(row+1)
                queen_col[row] = -1
    
    solutions = [0]
    queen_col = [-1] * n
    backtrack(0)
    return solutions[0]