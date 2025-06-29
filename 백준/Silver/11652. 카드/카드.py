n = int(input())
arr = [int(input()) for _ in range(n)]

arr.sort()

cnt = 0
mxval = -(1 << 62)  # 아주 작은 수
mxcnt = 0

for i in range(n):
    if i == 0 or arr[i] == arr[i - 1]:
        cnt += 1
    else:
        if cnt > mxcnt:
            mxcnt = cnt
            mxval = arr[i - 1]
        cnt = 1  # 새로운 숫자 시작

# 마지막 숫자 그룹 체크
if cnt > mxcnt:
    mxval = arr[n - 1]

print(mxval)
