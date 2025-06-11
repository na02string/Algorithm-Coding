n,m = map(int,input().split())
dic = {}
for ind in range(1,n+m+1):
    pok = str(input())
    if ind <= n:
        dic[pok] = ind
        dic[str(ind)] = pok
    else:
        print(dic[pok])