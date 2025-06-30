def solution(citations):
    citations.sort(reverse = True)
    answer = 0
    for i in range(len(citations)):
        if citations[i] <= (i+1):
            answer = max(answer,citations[i])
            break
        else:
            answer = min(i+1,citations[i])
    return answer
                
    