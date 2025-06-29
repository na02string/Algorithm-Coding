n = int(input())
from collections import deque
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
arr = deque(arr)

val = arr.popleft()
count = 1
max_count = 0
max_val = val
while arr:
    i = arr.popleft()
    if val == i:
        count += 1
        val = i
    else:
        if count>max_count:
            max_count = count
            max_val = val
        val = i
        count = 1
# 마지막 그룹 체크
if count > max_count:
    max_val = val
     
print(max_val)