n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
    
arr.sort()
answer = -1
for ind,val in enumerate(arr):
    answer = max(answer, val*(n-ind))
print(answer)    