import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())  # n: 정점 수, m: 간선 수
board = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    board[u].append(v)
    board[v].append(u)

visited = [False] * (n + 1)
answer = 0

def dfs(start_node):
    s = [start_node]
    visited[start_node] = True

    while s:
        cur = s.pop()
        for next in board[cur]:
            if visited[next]:
                continue
            s.append(next)
            visited[next] = True

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        answer += 1

print(answer)
