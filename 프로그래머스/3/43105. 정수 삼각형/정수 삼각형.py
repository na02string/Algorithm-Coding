def solution(triangle):
    dp = [[-1]*(i+2) for i in range(len(triangle)+1)]
    triangle.insert(0,[])
    for i in triangle:
        i.insert(0,-1)
    # print(triangle)
    dp[1][1] = triangle[1][1]
    # print(dp)
    for i in range(2, len(triangle)):
        for j in range(1,i+1):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
    answer = max(dp[-1])
    return answer

