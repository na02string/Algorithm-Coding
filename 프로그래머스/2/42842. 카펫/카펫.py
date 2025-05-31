def solution(brown, yellow):
    import math
    answer = []
    for alpha in range(1,int(math.sqrt(yellow))+1):
        if yellow % alpha == 0:
            beta = yellow / alpha
            if brown == 2*alpha + 2*beta + 4:
                break
    answer.append(beta+2)
    answer.append(alpha+2)
    return answer