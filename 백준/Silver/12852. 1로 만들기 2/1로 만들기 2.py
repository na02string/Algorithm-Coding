n = int(input())
D = [[0,[]] for i in range(n+1)]
D[1][1].append(1)
if n >= 2:
    D[2][0] = 1
    D[2][1].append(2); D[2][1].append(1)
for i in range(3,n+1):
    D[i][0] = D[i-1][0] + 1
    new_li = [i]+(D[i-1][1])
    D[i][1] = new_li
    if (i % 2 == 0) and (D[int(i/2)][0]+1 < D[i][0]):
        D[i][0] = D[int(i/2)][0]+1
        new_li = [i]+(D[int(i/2)][1])
        D[i][1] = new_li
    if (i % 3 == 0) and (D[int(i/3)][0]+1 < D[i][0]):
        D[i][0] = D[int(i/3)][0]+1
        new_li = [i]+(D[int(i/3)][1])
        D[i][1] = new_li
print(D[n][0])
print(' '.join(map(str,D[n][1])))