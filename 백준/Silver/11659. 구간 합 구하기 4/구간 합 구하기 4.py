import sys
input = sys.stdin.readline
n,m = map(int,input().split())
li = [0]
li.extend(list(map(int,input().split())))

# D[i] = li[1] + ... + li[i] = D[i-1] + A[i]
# a번째에서 b번째까지는 D[b] - D[a-1]
D = [0]*(n+1)
D[1] = li[1]
if n>= 2:
    for i in range(2, n+1):
        D[i] = D[i-1] + li[i]
for _ in range(m):
    a,b = map(int, input().split())
    answer = D[b] - D[a-1]
    print(answer)