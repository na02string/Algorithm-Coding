n = int(input())
meetings = []

for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((end, start))  # 종료 시간 기준 정렬 위해 순서 바꿈

meetings.sort()  # 기본적으로 튜플은 첫 번째 요소 기준 정렬됨

ans = 0
t = 0

for end, start in meetings:
    if t > start:
        continue
    ans += 1
    t = end

print(ans)
