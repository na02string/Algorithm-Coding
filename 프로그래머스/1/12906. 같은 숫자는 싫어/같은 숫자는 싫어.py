def solution(arr):
    from collections import deque
    arr = deque(arr)
    answer = []
    while arr:
        curr_value = arr.popleft()
        if answer:
            if answer[-1] == curr_value:
                pass
            else:
                answer.append(curr_value)
        else:
            answer.append(curr_value)
    return answer