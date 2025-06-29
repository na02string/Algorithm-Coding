def solution(scoville, K):
    import heapq 
    heapq.heapify(scoville) # 리스트를 우선순위 힙으로
    answer = 0
    
    
    while scoville[0] < K:
        if len(scoville) == 1: # 1개까지 가도 스코빌 지수가 안넘었으면
            return -1
        min1 = heapq.heappop(scoville) # k보다 작다는 제일 작은 수
        min2 = heapq.heappop(scoville)
        
        mix = min1 + min2*2
        answer += 1
                
        heapq.heappush(scoville, mix)
    
    return answer