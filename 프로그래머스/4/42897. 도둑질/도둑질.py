def making_dp(money):
    n = len(money)
    money.insert(0,0) # 더미 변수 추가
    dp = [0] * len(money)
    
    if n >= 1:
        dp[1] = money[1]
    if n>= 2:
        dp[2] = money[2]
    if n>= 3:
        dp[3] = dp[1] + money[3]
    for i in range(4, len(money)):
        dp[i] = max(dp[i-2]+money[i], dp[i-3] + money[i])
    # print(dp)
    return dp
    
def solution(money):
    # 1. 첫번째 집 무조건 선택하는 경우
    money1 = money.copy()[2:-1]
    n1 = len(money1)
    if n1 == 0:
        compare1 = money[0]
    else:
        # elif n1
        dp1 = making_dp(money1)
        # print(dp1)
        compare1 = max(dp1[-1], dp1[-2]) + money[0]
    
    # 2. 첫번재 집 선택 하지 않는 경우
    money2 = money.copy()[1:]
    dp2 = making_dp(money2)
    compare2 = max(dp2[-1], dp2[-2])
    
    answer = max(compare1,compare2)
    return answer