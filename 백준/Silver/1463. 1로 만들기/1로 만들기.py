num = int(input())

d = [0]*(num+1)
for i in range(2,num+1):
    replace = d[i-1] + 1
    
    if i % 2 == 0:
        replace = min(replace, d[i//2]+1)
    if i %3 == 0:
        replace = min(replace , d[i//3]+1)
    d[i] = replace
    
print(d[num])