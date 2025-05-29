def is_prime(num):
    import math
    if num <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True

def solution(numbers):
    from itertools import permutations
    answer = 0
    li = list(numbers)
    # print(li) # [0, 1, 1]
    # li로 만들 수 있는 모든 수 조합들 집합
    combination = set()
    for i in range(1,len(li)+1):
        tup = permutations(li,i)
        for j in tup:
            # print(int(''.join(j)))
            combination.add(int(''.join(j)))
            # print(combination)
    
    # 가능한 조합 모아둔 집합다 보면서 각각이 소수인지 판별하기
    for i in combination:
        if is_prime(i):
            answer += 1
    
    return answer