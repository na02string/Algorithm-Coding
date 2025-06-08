def solution(n, computers):
    # bfs 나 dfs로 탐색했을 때 탐색 끝나는게 연결 component 1개
    # 인접 행렬로 표현된 그래프
    from collections import deque
    answer = 0
    visited = [False] * n
    for i in range(n):
        if visited[i]:
            continue

        answer += 1
        q = deque()
        q.append(i)
        visited[i] = True
        
        while q:
            curr = q.popleft()
            for ind, nex in enumerate(computers[curr]):
                if nex == 0:
                    continue
                if ind == curr:
                    continue
                if not visited[ind]:
                    q.append(ind)
                    visited[ind] = True
    
    return answer