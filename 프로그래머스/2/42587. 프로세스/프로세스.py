def solution(priorities, location):
    from collections import deque
    answer = 0 # 종료된 수
    mark = deque(range(0,len(priorities))) 
    priorities = deque(priorities)
    
    a = True
    max_pri = max(priorities)
    
    while a:
        pri = priorities.popleft()
        mark_pop = mark.popleft()
        
        if pri == max_pri and priorities:
            max_pri = max(priorities)
        
        # 현재 pri의 우선순위가 가장 높은 경우 -> 프로세스 종료
        if pri >= max_pri:
            answer += 1 
            if mark_pop == location:
                return answer
        # 지금보다 더 높은 우선순위가 큐에 남은 경우 -> 뒤에 추가
        else:
            priorities.append(pri)
            mark.append(mark_pop)
    
