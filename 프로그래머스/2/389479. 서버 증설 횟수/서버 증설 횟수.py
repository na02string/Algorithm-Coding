from collections import deque
def solution(players, m, k):
    answer = 0
    
    curr_server = deque()
    curr_time = deque()
    for i in players:
        if curr_time:
            curr_time = deque([i-1 for i in curr_time]) 
            if curr_time[0] == 0:
                curr_server.popleft()
                curr_time.popleft()                        
        if i//m > sum(curr_server):
            answer += i//m - sum(curr_server)
            curr_server.append( i//m - sum(curr_server))
            curr_time.append(k)
        else:
            continue
    return answer