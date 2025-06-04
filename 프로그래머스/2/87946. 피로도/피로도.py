def solution(k, dungeons):
    answer = 0
    max_answer = 0
    input_k = k
    from itertools import permutations
    
    for i in permutations(dungeons):
        max_answer = max(answer, max_answer)
        answer = 0
        k = input_k
        if max_answer == len(i):
            break
        
        for j in i: #([80, 20], [50, 40], [30, 10])
            if k >= j[0]:
                k -= j[1]
                answer += 1
            else:
                pass
                
    return max_answer