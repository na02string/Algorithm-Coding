def bfs(n, adj):
    visited = [False] * (n+1)
    from collections import deque
    q = deque()
    q.append(1)
    visited[1] = True
    
    while q:
        curr = q.popleft()
        
        for nxt in adj[curr]:
            if visited[nxt]:
                continue
            q.append(nxt)
            visited[nxt] = True
            
    a = sum(visited)
    b = n - a
    # print(a,b)
    return abs(a-b)
            
    
    
def solution(n, wires):
    answer = 101
    for i in range(n-1):
        wires_copy = wires[:i]+wires[i+1:]
        # print(wires_copy)
        adj = [[] for _ in range(n+1)]
        # 방문한 노드 체크
        for s,e in wires_copy:
            adj[s].append(e)
            adj[e].append(s)
        
        candidate = bfs(n,adj)
        answer = min(answer, candidate)
        
    return answer