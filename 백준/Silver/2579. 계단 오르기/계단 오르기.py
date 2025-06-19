n = int(input())
stair = [0]
for _ in range(n):
    stair.append(int(input()))

D = [[0,0,0] for _ in range(n+1)]
D[1][1] = stair[1]
if n > 1:
    D[2][1] = stair[2]
    D[2][2] = stair[1] + stair[2]
for i in range(3,n+1):
    D[i][1] = max(D[i-2][1], D[i-2][2]) + stair[i]
    D[i][2] = D[i-1][1] + stair[i]
print(max(D[n][1], D[n][2]))