import sys
input = sys.stdin.readline

N,M = map(int, input().split())
rs = []
visited = [False] * (N+1)

def recur(num):
    if num == M:
        print(' '.join(map(str,rs)))
        return
    
    for i in range(1,N+1):
        if visited[i] == False:
            rs.append(i)
            visited[i] = True
            recur(num+1)
            rs.pop()
            visited[i] = False

recur(0)            
    