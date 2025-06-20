num = int(input())
color = [[0] for _ in range(num+1)]
for i in range(1,num+1):
    color[i].extend(list(map(int, input().split())))
D = [[0, 0, 0, 0] for _ in range(num+1)]
# D[i][j] = i번째 집을 j색으로 칠했을 때의 최소 비용
D[1][1] = color[1][1]
D[1][2] = color[1][2]
D[1][3] = color[1][3]
for i in range(1,num+1):
    D[i][1] = min(D[i-1][2], D[i-1][3]) + color[i][1]
    D[i][2] = min(D[i-1][1], D[i-1][3]) + color[i][2]
    D[i][3] = min(D[i-1][1], D[i-1][2]) + color[i][3]
print(min(D[num][1], D[num][2], D[num][3]))