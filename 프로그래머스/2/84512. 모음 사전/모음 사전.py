from itertools import product
def solution(word):
    answer = 0
    candidate = [ 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(1,6):
        for p in product(candidate, repeat = i):
            result.append(''.join(p))
    result.sort()            
    return result.index(word) + 1