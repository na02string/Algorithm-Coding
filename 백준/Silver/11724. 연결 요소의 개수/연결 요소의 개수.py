import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
board = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    board[u].append(v)
    board[v].append(u)

visited = [False] * (n + 1)
answer = 0

def dfs(start_node):
    stack = [start_node]
    visited[start_node] = True

    while stack:
        cur = stack.pop()
        for next in board[cur]:
            if not visited[next]:
                visited[next] = True
                stack.append(next)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        answer += 1

print(answer)
