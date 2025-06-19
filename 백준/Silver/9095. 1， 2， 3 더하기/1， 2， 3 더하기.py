n = int(input())
def sol(num):
    d = [1]*(num+1)
    for i in range(2,num+1):
        if i == 2:
            d[i] = d[i-1] + d[i-2]
        else:
            d[i] = d[i-1] + d[i-2] + d[i-3]
    print(d[num])
    
for _ in range(n):
    num = int(input())
    sol(num)