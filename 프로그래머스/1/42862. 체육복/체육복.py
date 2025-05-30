def solution(n, lost, reserve):
    # 여분있는 애 기준으로 앞에 애가 도난이면 걔면저 주기
    from collections import deque
    
    lost_set = set(lost)
    reserve_set = set(reserve)
    intersect = lost_set.intersection(reserve_set)
    lost_set = lost_set - intersect
    reserve_set = reserve_set - intersect
    
    
    reserve = deque(sorted(reserve_set))
    lost = deque(sorted(lost_set))
    
    
    still_lost = []
    while True:
        if lost:
            fill_candidate = lost.popleft()
            if fill_candidate -1 in reserve:
                reserve.remove(fill_candidate - 1)
                continue
            elif fill_candidate + 1 in reserve:
                reserve.remove(fill_candidate+1)
                continue
            else:
                still_lost.append(fill_candidate)
        else:
            break    
    answer = n - len(still_lost)
    
    return answer