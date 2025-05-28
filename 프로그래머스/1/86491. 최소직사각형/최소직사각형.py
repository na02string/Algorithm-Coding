def solution(sizes):
    # 명함 리스트에서 각 명함에서 긴 부분을 가로, 짧은 부분을 세로 길이라고 정리시키기
    # 그 상태에서 모든 가로 중 max, 세로 중 max 만 곱하면 됨
    for ind, size in enumerate(sizes):
        w = size[0]; h = size[1]
        new_w = max(w,h)
        new_h = min(w,h)
        sizes[ind] = [new_w,new_h]
        
    max_w = 0; max_h = 0
    for size in sizes:
        w = size[0]; h = size[1]
        if w > max_w:
            max_w = w
        if h > max_h:
            max_h = h
    
    return max_h*max_w