def calcul(n1_set,n2_set):
    # 사칙연산 결과 뱉어내기
    li = []
    for n1 in n1_set:
        for n2 in n2_set:
            a = n1 + n2
            b = n1 - n2
            c = n1 * n2
            li.extend([a,b,c])
            try:
                d = n1 // n2
            except ZeroDivisionError:
                continue
            li.append(d)
    return li


def solution(N, number):
    answer = -1
    dp = [set() for _ in range(9)]
    
    dp[1].add(N)
    if number == N:
        return 1
    
    for i in range(2,9):
        dp[i].add(int(str(N)*i))
        for j in range(1,i):
            dp[i].update(calcul(dp[j], dp[i-j]))
        
        if number in dp[i]:
            return i
        
    return answer

