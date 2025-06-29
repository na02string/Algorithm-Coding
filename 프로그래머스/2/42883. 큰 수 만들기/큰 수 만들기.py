def solution(number, k):

    s = []
    from collections import deque
    number = deque(list(number))
    
    curr = number.popleft() # 9
    s.append(curr)
    while number: # 24
        curr = number.popleft() # number 24
        while s and curr> s[-1] and k>0:
            s.pop(-1)
            k-=1
        s.append(curr)

    if k>0:
        s = s[:-k]
            
    return ''.join(s)