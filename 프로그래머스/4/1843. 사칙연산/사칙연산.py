def solution(arr):
    num_arr = [0]
    calc_arr= [0]
    for i in arr:
        try:
            a = int(i)
            num_arr.append(a)
        except:
            if i == '-':
                calc_arr.append(-1)
            else:
                calc_arr.append(1)
    dp_min = [[0]*(len(num_arr)+1) for _ in range(len(num_arr)+1)]
    dp_max = [[0]*(len(num_arr)+1) for _ in range(len(num_arr)+1)]
    
    # 구간 사이즈 1인거 먼저 초기화
    for i in range(1,len(num_arr)): # 자기 자신만 있는 구간 초기화
        dp_min[i][i] = num_arr[i] 
        dp_max[i][i] = num_arr[i]
        
    # 구간 사이즈 작은 것부터 초기화 해야함
    for size in range(1,len(num_arr)-1): # 5-1 = 4
        # size가 2면 1~3, 2~4 까지 가능. 이때 num_arr 크기는 5
        # end 는 num_arr -1 -size까지가 범위
        start = 1 ; end = len(num_arr) - 1 - size # 시작 인덱스의 가능 범위
        for i in range(start, end+1):
            dp_min[i][i+size] = float('inf')
            dp_max[i][i+size] = -float('inf')
            for k in range(i,i+size):
                if calc_arr[k] == -1:
                    dp_min[i][i+size] = min(dp_min[i][i+size], dp_min[i][k] - dp_max[k+1][i+size])
                    dp_max[i][i+size] = max(dp_max[i][i+size], dp_max[i][k] - dp_min[k+1][i+size])
                else: # 중간에 연산자가 + 인 경우
                    dp_min[i][i+size] = min(dp_min[i][i+size], dp_min[i][k] + dp_min[k+1][i+size])
                    dp_max[i][i+size] = max(dp_max[i][i+size], dp_max[i][k] + dp_max[k+1][i+size])
    
    return dp_max[1][len(num_arr)-1]

