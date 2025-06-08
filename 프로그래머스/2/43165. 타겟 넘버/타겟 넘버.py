def solution(numbers, target):
    answer = 0
    from collections import deque
    q = deque()
    q.append((0,0)) # index, 총합
    
    while q:
        index, total = q.popleft()
        if index < len(numbers):
            next_node = [numbers[index], numbers[index]*(-1)]
            for i in next_node:
                q.append((index+1, total + i))
        if (index == len(numbers)):
            if (total == target):
                answer += 1
    return answer