n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# Please write your code here.
for target in queries:
    left = 0
    right = len(arr) -1
    exist = -2

    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == target:
            exist = mid
            break

        if arr[mid] >= target:
            right = mid-1
        else:
            left = mid+1
    
    print(exist +1 )