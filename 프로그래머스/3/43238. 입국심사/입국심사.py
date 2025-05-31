def solution(n, times):
    answer = 0
    # 최대로 걸릴 수 있는 시간 기준으로 이분탐색해 나가면서 가장 작은 시간 찾기
    start = 1
    end = max(times) * n
    min_idx = end + 1
    
    mid = (start + end) // 2
    while start<=end:
        total = sum(mid//i for i in times)
        if total >= n:
            end = mid-1
            min_idx = min(min_idx,mid)
            mid = (start+end) // 2
            continue
        elif total < n:
            start = mid +1 
            mid = (start + end) //2 
            continue
    # print(min_idx)
    return min_idx