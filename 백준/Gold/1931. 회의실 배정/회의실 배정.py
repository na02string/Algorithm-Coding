# 끝나는 시간이 가장 빠른 순서대로 정렬하고
#선택할 수 있는 회의 중 끝나는 시간이 가장 빠른 회의 선택해나가는 방법
n = int(input())
meeting = []
for _ in range(n):
    meeting.append(list(map(int,input().split())))
meeting.sort(key = lambda x : (x[1], x[0])) # 끝나는 시간 기준 정렬하고
# 끝나는 시간이 같으면 시작시간 기준정렬
from collections import deque
meeting = deque(meeting)
answer = 0
last_end= 0
while meeting:
    start, end = meeting.popleft()
    
    if start>= last_end:
        answer += 1
        last_end = end # 직전에 끝난 회의 시간
           
print(answer)          