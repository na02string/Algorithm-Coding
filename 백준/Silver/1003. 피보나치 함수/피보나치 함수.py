n = int(input())
li = []
for _ in range(n):
    li.append(int(input()))
max_li = max(li)
D = [[0,0] for _ in range(max_li + 1)] # 0호출 횟수, 1호출 횟수
D[0][0] = 1
if max_li >= 1:
    D[1][1] = 1
    for i in range(2, max_li + 1):
        D[i][0] = D[i-1][0] + D[i-2][0]
        D[i][1] = D[i-1][1] + D[i-2][1]
for i in li:
    print(D[i][0], D[i][1])