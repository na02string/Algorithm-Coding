def solution(n, edge):
    # BFS 로 탐색하면서 거리잰거 VISITED배열에 남기기
    # 탐색 끝나면 visited에서 값 제일 큰 수 구하고 그거 갯수 구하면 될듯
    adj = [[] for _ in range(n+1)]
    visited = [False]*(n+1)
    for i in edge:
        u = i[0]
        v = i[1]
        adj[u].append(v)
        adj[v].append(u)
        
    from collections import deque
    q = deque()
    q.append(1)
    visited[1] = 1
    
    while q:
        curr = q.popleft()
        
        for next in adj[curr]:
            if visited[next] != False: # 방문한적 있는 노드면 패스
                continue
            q.append(next)
            visited[next] = visited[curr] + 1
    
    max_visited = max(visited)
    answer = visited.count(max_visited)
    return answer